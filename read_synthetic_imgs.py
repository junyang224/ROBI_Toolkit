import cv2
import numpy as np
import os
import inout
import matplotlib.pyplot as plt

np.set_printoptions(precision=8, suppress=True)

# Dataset Info
######################################
# Path to the ROBI dataset
data_path = '/Add/your/path/here/ROBI_Synthetic/'
obj = 'Zigzag_synthetic' # Object Name
# Camera sensor to use
sensor = 'Ensenso'
is_visualize = True
######################################



# Camera Info
#######################################################
cam_info_path = os.path.join('./cam', '{}.yml')
cam_DEPTH_path = cam_info_path.format(sensor+'_DEPTH')
cam_LEFT_path = cam_info_path.format(sensor+'_LEFT')
cam_RIGHT_path = cam_info_path.format(sensor+'_RIGHT')

depth_info = inout.load_cam_info(cam_DEPTH_path)
LEFT_info = inout.load_cam_info(cam_LEFT_path)

depth_unit = depth_info['depth_unit']
depth_fx = depth_info['fx']
depth_fy = depth_info['fy']
depth_cx = depth_info['cx']
depth_cy = depth_info['cy']
left_fx = LEFT_info['fx']
left_fy = LEFT_info['fy']
left_cx = LEFT_info['cx']
left_cy = LEFT_info['cy']
#######################################################


# Data path Info
########################################################################################################
synthetic_scene_path = os.path.join(data_path, obj)
for json_name in os.listdir(synthetic_scene_path):
    if json_name.endswith('.json'):
        left_name = json_name.replace(".json", "_Left.png")
        mask_name = json_name.replace(".json", "_Mask.png")
        depth_name = json_name.replace(".json", "_Depth.png")
        JSON_path = os.path.join(synthetic_scene_path, json_name)
        DEPTH_path = os.path.join(synthetic_scene_path, depth_name)
        MASK_path = os.path.join(synthetic_scene_path, mask_name)
        LEFT_path = os.path.join(synthetic_scene_path, left_name)

        # Load Images
        depth_img = cv2.imread(DEPTH_path, cv2.IMREAD_ANYDEPTH) * depth_unit
        left_img = cv2.imread(LEFT_path, cv2.IMREAD_UNCHANGED)
        mask_img = cv2.imread(MASK_path, cv2.IMREAD_UNCHANGED)
        mask_img = mask_img[:, :, 2]

        # Load Object Poses, Visibility Score and Mask Image
        scene_info = inout.load_sceneInfo(JSON_path)
        T_world2cam = np.array(scene_info["T_world2cam"]).reshape(4,4)
        num_obj = len(scene_info)

        for obj_idx in range(2, num_obj+1):
            obj_name_idx = "Object_" + str(obj_idx)
            # Object visibility
            visibility_score_idx = float(scene_info[obj_name_idx]["visibility"])
            # Object mask image
            mask_id_idx = int(scene_info[obj_name_idx]["mask_id"])
            mask_img_idx = (mask_img == mask_id_idx).astype(np.uint8) * 255
            # Object pose
            T_world2obj_idx = np.array(scene_info[obj_name_idx]["T_world2obj"]).reshape(4,4)
            T_cam2obj_idx = np.matmul(np.linalg.inv(T_world2cam), T_world2obj_idx)

            if is_visualize:
                plt.figure()
                plt.subplot(1, 3, 1)
                plt.imshow(left_img)
                plt.subplot(1, 3, 2)
                plt.imshow(depth_img)
                plt.subplot(1, 3, 3)
                plt.imshow(mask_img_idx)
                plt.show()


            a = 1
########################################################################################################



