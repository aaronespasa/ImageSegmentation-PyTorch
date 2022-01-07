"""
This dataset can be found using the following URL:
https://www.kaggle.com/c/carvana-image-masking-challenge

Copyright (c), Aarón Espasandín - All Rights Reserved

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree:
https://github.com/aaronespasa/ImageSegmentation-PyTorch/blob/main/LICENSE
"""
import os
from PIL import Image
from torch.utils.data import Dataset
import numpy as np

# IMG_DIR = 'downloads/carvana/train'
# MASK_DIR = 'downloads/carvana/train_masks'

class CarvanaDataset(Dataset):
    """Class to process the Carvana Dataset.
    
    It's a subclass of the PyTorch dataset.
    """
    def __init__(self, img_dir, mask_dir, transform=None):
        self.img_dir = img_dir
        self.mask_dir = mask_dir
        self.transform = transform
        self.images = os.listdir(img_dir)

    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.images[idx])
        mask_path = os.path.join(self.mask_dir, self.images[idx].replace(".jpg", "_mask.gif"))

        img = np.array(Image.open(img_path).convert("RGB")) # rgb
        mask = np.array(Image.open(mask_path).convert("L"), dtype=np.float32) # grayscale

        # We're going to use the sigmoid activation function. Therefore,
        # it's better to convert the black part from the image from 255 to 1
        mask[mask == 255.0] = 1.0

        if self.transform is not None:
            augmentations = self.transform(img=img, mask=mask)
            img = augmentations["img"]
            mask = augmentations["mask"]

        return img, mask