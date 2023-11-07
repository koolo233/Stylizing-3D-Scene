import os
import json
import argparse


parser = argparse.ArgumentParser(description='split data')
parser.add_argument('--data_dir', type=str, default='data', help='path to data folder')
parser.add_argument('--out_dir', type=str, required=True, help='path to output folder')
parser.add_argument('--data_type', type=str, default='llff', help='data type of the dataset')
args = parser.parse_args()


def save_data(output_dir, save_image, save_data):
    image_base_name = os.path.splitext(save_image)[0]

    # save image, intrinsics, pose
    image_path = os.path.join(posed_images_folder, 'images', save_image)
    out_image_path = os.path.join(output_dir, 'rgb', save_image)
    os.makedirs(os.path.dirname(out_image_path), exist_ok=True)
    # copy data to new folder
    os.system(f'cp {image_path} {out_image_path}')

    # save intrinsics
    intrinsics_out_path = os.path.join(output_dir, 'intrinsics', f'{image_base_name}.txt')
    os.makedirs(os.path.dirname(intrinsics_out_path), exist_ok=True)
    with open(intrinsics_out_path, 'w') as f:
        f.write(' '.join([str(n) for n in save_data['K']]))

    # save pose
    pose_out_path = os.path.join(output_dir, 'pose', f'{image_base_name}.txt')
    os.makedirs(os.path.dirname(pose_out_path), exist_ok=True)
    with open(pose_out_path, 'w') as f:
        f.write(' '.join([str(n) for n in save_data['W2C']]))



if __name__ == "__main__":

    mvs_folder = os.path.join(args.data_dir, 'mvs')
    posed_images_folder = os.path.join(args.data_dir, 'posed_images')
    sfm_folder = os.path.join(args.data_dir, 'sfm')

    # load cameras.json
    cameras_json_path = os.path.join(posed_images_folder, 'kai_cameras.json')
    with open(cameras_json_path, 'r') as f:
        cameras_json = json.load(f)

    # load cameras_normalized.json
    cameras_normalized_json_path = os.path.join(posed_images_folder, 'kai_cameras_normalized.json')
    with open(cameras_normalized_json_path, 'r') as f:
        cameras_normalized_json = json.load(f)

    # split test/val/train
    os.makedirs(args.out_dir, exist_ok=True)
    os.makedirs(os.path.join(args.out_dir, 'test'), exist_ok=True)
    os.makedirs(os.path.join(args.out_dir, 'train'), exist_ok=True)
    os.makedirs(os.path.join(args.out_dir, 'validation'), exist_ok=True)

    for image_id, key in enumerate(cameras_normalized_json.keys()):
        image_name = key
        image_data = cameras_normalized_json[key]

        if image_id % 8 == 0:
            save_data(os.path.join(args.out_dir, 'test'), image_name, image_data)
            save_data(os.path.join(args.out_dir, 'validation'), image_name, image_data)
        else:
            save_data(os.path.join(args.out_dir, 'train'), image_name, image_data)
