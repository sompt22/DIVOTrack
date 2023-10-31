cd src
python train.py mot --exp_id sompt22 --data_cfg "./lib/cfg/data_sompt22.json" --load_model "../models/divo_dla34.pth" --gpus 0 --batch_size 16 --num_epochs 30
cd ..
