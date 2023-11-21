import os
import glob
import _init_paths


def gen_caltech_path(root_path):
    label_path = 'DIVO/labels_with_ids/train'
    real_path = os.path.join(root_path, label_path)
    print(real_path)
    image_path = real_path.replace('labels_with_ids', 'images')
    print(image_path)
    images_exist = sorted(glob.glob(image_path + '/*.jpg'))
    print(len(images_exist))    
    with open('../src/data/divo.train', 'w') as f:
        labels = sorted(glob.glob(real_path + '/*.txt'))
        for label in labels:
            image = label.replace('labels_with_ids', 'images').replace('.txt', '.jpg')
            if image in images_exist:
                print(image[22:], file=f)
    f.close()


def gen_data_path(root_path):
    mot_path = 'MOT17/images/train'
    real_path = os.path.join(root_path, mot_path)
    seq_names = [s for s in sorted(os.listdir(real_path)) if s.endswith('SDP')]
    with open('/home/yfzhang/PycharmProjects/fairmot/src/data/mot17.half', 'w') as f:
        for seq_name in seq_names:
            seq_path = os.path.join(real_path, seq_name)
            seq_path = os.path.join(seq_path, 'img1')
            images = sorted(glob.glob(seq_path + '/*.jpg'))
            len_all = len(images)
            len_half = int(len_all / 2)
            for i in range(len_half):
                image = images[i]
                print(image[22:], file=f)
    f.close()

def gen_data_path(root_path):
    mot_path = 'divo/images/train'
    real_path = os.path.join(root_path, mot_path)
    seq_names = [s for s in sorted(os.listdir(real_path))]
    with open('/home/fatih/phd/DIVOTrack/Single_view_Tracking/FairMOT/src/data/sompt22.train', 'w') as f:
        for seq_name in seq_names:
            seq_path = os.path.join(real_path, seq_name)
            seq_path = os.path.join(seq_path, 'img1')
            images = sorted(glob.glob(seq_path + '/*.jpg'))
            len_all = len(images)
            len_half = int(len_all / 2)
            for i in range(len_all):
                image = images[i]
                print(image[35:], file=f)
    f.close()





def gen_data_path_mot17_val(root_path):
    mot_path = 'MOT17/images/train'
    real_path = os.path.join(root_path, mot_path)
    seq_names = [s for s in sorted(os.listdir(real_path)) if s.endswith('SDP')]
    with open('/home/yfzhang/PycharmProjects/fairmot2/src/data/mot17.val', 'w') as f:
        for seq_name in seq_names:
            seq_path = os.path.join(real_path, seq_name)
            seq_path = os.path.join(seq_path, 'img1')
            images = sorted(glob.glob(seq_path + '/*.jpg'))
            len_all = len(images)
            len_half = int(len_all / 2)
            for i in range(len_half, len_all):
                image = images[i]
                print(image[22:], file=f)
    f.close()


def gen_data_path_mot17_emb(root_path):
    mot_path = 'MOT17/images/train'
    real_path = os.path.join(root_path, mot_path)
    seq_names = [s for s in sorted(os.listdir(real_path)) if s.endswith('SDP')]
    with open('/home/yfzhang/PycharmProjects/fairmot2/src/data/mot17.emb', 'w') as f:
        for seq_name in seq_names:
            seq_path = os.path.join(real_path, seq_name)
            seq_path = os.path.join(seq_path, 'img1')
            images = sorted(glob.glob(seq_path + '/*.jpg'))
            len_all = len(images)
            len_half = int(len_all / 2)
            for i in range(len_half, len_all, 3):
                image = images[i]
                print(image[22:], file=f)
    f.close()


if __name__ == '__main__':
    root = '/home/fatih/phd/DIVOTrack/datasets/'
    gen_data_path(root)
