cd src
python train.py mot --exp_id sompt22 --data_cfg "./lib/cfg/data_sompt22.json" --load_model "../models/crowdhuman_dla34.pth" --gpus 0 --batch_size 8 --num_epochs 30
cd ..
