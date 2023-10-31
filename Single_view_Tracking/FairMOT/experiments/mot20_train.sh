cd src
python train.py mot --exp_id mot20 --data_cfg "./lib/cfg/data_mot20.json" --load_model "../models/divo_dla34.pth" --gpus 0 --batch_size 16 --num_epochs 30
cd ..
