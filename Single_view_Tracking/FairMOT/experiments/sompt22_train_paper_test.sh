cd src
python track.py mot --exp_name sompt22_train_10secs_occlusion --load_model "/home/fatih/phd/models_sompt22/fairmot/logs_2023-10-30-22-04/model_last.pth" --test_sompt22_train_10secs_occlusion True --conf_thres 0.5 --gpus 0
cd ..
