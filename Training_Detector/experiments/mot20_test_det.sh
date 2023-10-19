cd src
python test_det.py mot --exp_id mot20_test_det --load_model '../exp/mot/train_det/model_det_last.pth' --data_cfg '../src/lib/cfg/data_mot20.json' --gpus 0
cd ..
