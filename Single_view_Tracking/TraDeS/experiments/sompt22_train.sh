cd src
python main.py tracking --exp_id trades_sompt22 --dataset sompt22 --pre_hm --ltrb_amodal --same_aug --hm_disturb 0.05 --lost_disturb 0.4 --fp_disturb 0.1 --gpus 0 --save_point 10,20,25,30 --load_model ../models/crowdhuman.pth --clip_len 3 --max_frame_dist 10  --batch_size 6 --trades
cd ..
