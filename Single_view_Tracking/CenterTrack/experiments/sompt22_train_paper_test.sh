cd src
python test.py tracking --exp_id sompt22-train-10secs-occlusion --dataset sompt22-train-10secs-occlusion --pre_hm --ltrb_amodal --track_thresh 0.4 --pre_thresh 0.5 --load_model "/home/fatih/phd/models_sompt22/centertrack/model_last.pth"
cd ..