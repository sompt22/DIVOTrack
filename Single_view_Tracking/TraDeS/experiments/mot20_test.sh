cd src
python test.py tracking --exp_id trades_mot20 --dataset mot20 --pre_hm --ltrb_amodal --pre_thresh 0.5 --inference --clip_len 3 --track_thresh 0.4 --gpus 0 --trades --resume
cd ..
