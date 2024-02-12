#!/bin/bash

# This script runs inference on a video file

model_path=$(realpath $1)
video_path=$(realpath $2)

echo "$video_path"
echo "$model_path"

_experiment_name=$(basename "$video_path" | cut -f1 -d'.')
experiment_name='inference_'$_experiment_name
printf "experiment_name: $experiment_name\n"

cd src
# infer --motchallenge saves inference results
python demo.py mot --load_model $model_path --input-video $video_path --conf_thres 0.4
cd ..
