cd src
python track.py mot --exp_name inference --load_model ../exp/mot/sompt22/model_last.pth --test_sompt22 True --conf_thres 0.5 
cd ..
