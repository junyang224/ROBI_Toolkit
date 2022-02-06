# ROBI_Toolkit
Python scripts to work on the ROBI dataset - a multi-view dataset for reflective objects in robotic bin-picking (available at: https://www.trailab.utias.utoronto.ca/robi).

# Requirements
Python >=3.5 \
opencv-python >= 3.1 \
numpy\
ruamel.yaml

# Baseline Methods
We provide the evaluation results on three object pose estimators (PPF, Line2D, AAE), reasearchers are welcome to compare them against their our methods. The evaluation results can be download [here](https://drive.google.com/file/d/1Ru3fmcYFBGOufGUp2jCkFaQgLCv7spIh/view?usp=sharing).

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

# Citation
If you find ROBI dataset useful in your research, please consider citing:

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
