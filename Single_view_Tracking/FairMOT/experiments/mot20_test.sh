cd src
python track.py mot --exp_name mot20 --load_model ../exp/mot/mot20/model_last.pth --test_mot20 True --conf_thres 0.5 --gpus 0
cd ..
