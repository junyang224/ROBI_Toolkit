# ROBI_Toolkit
Python scripts to work on the ROBI dataset - a multi-view dataset for reflective objects in robotic bin-picking (available at: https://www.trailab.utias.utoronto.ca/robi).

# Requirements
Python >=3.5 \
opencv-python >= 3.1 \
numpy\
ruamel.yaml

# Baseline Methods
We provide the evaluation results on three object pose estimators (PPF [1], Line2D [2], AAE [3]), reasearchers are welcome to compare them against their our methods. The evaluation results can be download [here](https://drive.google.com/file/d/1Ru3fmcYFBGOufGUp2jCkFaQgLCv7spIh/view?usp=sharing).

# Code
read_scene_imgs.py: A script to load test images (with 6D camera poses and the ground truth 6D object poses).\
read_pattern_imgs.py: A script to load stereo pattern images and disparity maps. \
eval_baselines.py: A script to load ground truth object poses and the estimated object poses from provided baseline methods.

# Ground Truth Depth Map
Please note that, we capture the ground truth depth map with only Ensenso camera (no Realsense data). For Scene 4, 5, 8, 9, each viewpoint image has the corresponding GT depth map (in "GT_Depth" folder). For Scene 1, 2, 3, 6, 7, the GT depth maps were captured only for a subset of viewpoints in Ensenso data folder: \
For Scene 1-3: \
DEPTH_view_71-DEPTH_view_87 \
For Scene 6-7: \
DEPTH_view_12-DEPTH_view_14, DEPTH_view_16, DEPTH_view_18, DEPTH_view_22, DEPTH_view_24-DEPTH_view_41

# Author
Jun Yang\
junyang.yang@mail.utoronto.ca\
Institute for Aerospace Studies, University of Toronto

# References
[1] Drost, B., Ulrich, M., Navab, N., & Ilic, S. (2010, June). Model globally, match locally: Efficient and robust 3D object recognition. In 2010 IEEE computer society conference on computer vision and pattern recognition (pp. 998-1005). Ieee.\
[2] Hinterstoisser, S., Lepetit, V., Ilic, S., Holzer, S., Bradski, G., Konolige, K., & Navab, N. (2012, November). Model based training, detection and pose estimation of texture-less 3d objects in heavily cluttered scenes. In Asian conference on computer vision (pp. 548-562). Springer, Berlin, Heidelberg.\
[3] Sundermeyer, M., Marton, Z. C., Durner, M., Brucker, M., & Triebel, R. (2018). Implicit 3d orientation learning for 6d object detection from rgb images. In Proceedings of the european conference on computer vision (ECCV) (pp. 699-715).

# Citation
If you find ROBI dataset useful in your work, please consider citing:

    @inproceedings{yang2021robi,
      title={ROBI: A Multi-View Dataset for Reflective Objects in Robotic Bin-Picking},
      author={Yang, Jun and Gao, Yizhou and Li, Dong and Waslander, Steven L},
      booktitle={2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
      year={2021},
      organization={IEEE}
    }
    
    @article{yang2021probabilistic,
      title={Probabilistic Multi-View Fusion of Active Stereo Depth Maps for Robotic Bin-Picking},
      author={Yang, Jun and Li, Dong and Waslander, Steven L},
      journal={IEEE Robotics and Automation Letters},
      volume={6},
      number={3},
      pages={4472--4479},
      year={2021},
      publisher={IEEE}
    }
