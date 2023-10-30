cd src
python track.py mot --exp_name divo_test --load_model ../exp/mot/divo/model_last.pth --test_divo True --conf_thres 0.5 --gpus 0
cd ..