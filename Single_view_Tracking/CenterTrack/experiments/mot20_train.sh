cd src
python main.py tracking --exp_id mot20 --dataset mot20 --pre_hm --ltrb_amodal --same_aug --hm_disturb 0.05 --lost_disturb 0.4 --fp_disturb 0.1 --gpus 0 --load_model ../models/crowdhuman.pth --num_epochs 30 --batch_size 16
cd ..
