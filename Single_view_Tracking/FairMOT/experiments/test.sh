cd src
python track.py mot --exp_name inference --load_model ../exp/mot/train/model_fairmot.pth --test_divo_train True --conf_thres 0.5 --gpus 0
cd ..