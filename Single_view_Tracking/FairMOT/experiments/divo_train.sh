cd src
python train.py mot --exp_id divo --data_cfg "./lib/cfg/data_divo.json" --load_model "../models/crowdhuman_dla34.pth" --gpus 0 --batch_size 16 --num_epochs 30
cd ..