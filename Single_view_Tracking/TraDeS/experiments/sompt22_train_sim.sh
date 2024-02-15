cd src
python test.py tracking --exp_id trades_sompt22_train_sim --dataset sompt22-train-sim --pre_hm --ltrb_amodal --pre_thresh 0.5 --inference --clip_len 3 --track_thresh 0.4 --gpus 0 --trades --load_model "/home/fatih/phd/models_sompt22/trades/logs_2023-10-26-13-49/model_last.pth"
cd ..
