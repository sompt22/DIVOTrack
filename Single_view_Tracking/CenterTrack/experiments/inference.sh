#!/bin/bash

# This script runs inference on a video file
experiment_name=$1
model_path=$(realpath $2)
video_path=$(realpath $3)


cd src
# infer --motchallenge saves inference results
python demo.py tracking --exp_id $experiment_name --max_age 15 --debug 1 --load_model $model_path --num_classes 1 --demo $video_path 
cd ..
