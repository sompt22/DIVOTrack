cd src
python main.py tracking --exp_id sompt22 --dataset sompt22 --pre_hm --ltrb_amodal --val_intervals 1 --lr 1.25e-4 --same_aug --hm_disturb 0.05 --lost_disturb 0.4 --fp_disturb 0.1 --gpus 0 --load_model "../models/crowdhuman_divo_trained.pth" --num_epochs 30 --batch_size 16
cd ..
