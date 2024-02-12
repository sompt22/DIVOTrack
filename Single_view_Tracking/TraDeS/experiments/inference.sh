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
python demo.py tracking --load_model $model_path --num_classes 1 --demo $video_path --pre_hm --ltrb_amodal --pre_thresh 0.5 --track_thresh 0.5 --inference --clip_len 2 --trades --save_video --resize_video --input_h 480 --input_w 864
cd ..