# ROBI_Toolkit
Python scripts to work on the ROBI dataset - a multi-view dataset for reflective objects in robotic bin-picking (available at: https://www.trailab.utias.utoronto.ca/robi).

# Requirements
Python >=3.5 \
opencv-python >= 3.1 \
numpy\
ruamel.yaml

# Code
read_scene_imgs.py: A script to load test images (with 6D camera poses and the ground truth 6D object poses).\
read_pattern_imgs.py: A script to load stereo pattern images and disparity maps.

# Ground Truth Depth Map
Please note that, we capture the ground truth depth map with only Ensenso camera (no Realsense data). If you want to use the ground truth depth map (in "GT_Depth" folder), below is the the relationship between GT_Depth and Ensenso sensor folder:

For Scene 1-3: \
GT_Depth: view_0---view_16 ---> Ensenso/Depth: DEPTH_view_71---DEPTH_view_87

For Scene 4-5: \
GT_Depth: view_0---view_105 ---> Ensenso/Depth: DEPTH_view_0---DEPTH_view_105

For Scene 6-7: \
GT_Depth: view_0---view_2 ---> Ensenso/Depth: DEPTH_view_12---DEPTH_view_14 \
GT_Depth: view_3 ---> Ensenso/Depth: DEPTH_view_16 \
GT_Depth: view_4 ---> Ensenso/Depth: DEPTH_view_18 \
GT_Depth: view_5 ---> Ensenso/Depth: DEPTH_view_22 \
GT_Depth: view_6---view_23 ---> Ensenso/Depth: DEPTH_view_24---DEPTH_view_41

For Scene 8-9: \
GT_Depth: view_0---view_67 ---> Ensenso/Depth: DEPTH_view_0---DEPTH_view_67

# Author
Jun Yang\
junyang.yang@mail.utoronto.ca\
Institute for Aerospace Studies, University of Toronto
