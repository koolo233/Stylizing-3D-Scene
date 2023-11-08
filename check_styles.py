import os
from PIL import Image
from tqdm import tqdm

import warnings
warnings.filterwarnings('error')


if __name__ == "__main__":
    train_styles_folder = "./wikiart/train"
    test_styles_folder = "./wikiart/test"
    val_styles_folder = "./wikiart/validation"

    # check all images
    print("begin check training styles...")
    for style_name in tqdm(os.listdir(train_styles_folder)):
        image_path = os.path.join(train_styles_folder, style_name)
        try:
            with Image.open(image_path).convert('RGB'):
                pass
        except:
            print(image_path)
            os.system(f"rm {image_path}")

    print("begin check testing styles...")
    for style_name in tqdm(os.listdir(test_styles_folder)):
        image_path = os.path.join(test_styles_folder, style_name)
        try:
            img = Image.open(image_path).convert('RGB')
        except:
            print(image_path)
            os.system(f"rm {image_path}")

    print("begin check validation styles...")
    for style_name in tqdm(os.listdir(val_styles_folder)):
        image_path = os.path.join(val_styles_folder, style_name)
        try:
            img = Image.open(image_path).convert('RGB')
        except:
            print(image_path)
            os.system(f"rm {image_path}")
