import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2
from tqdm import tqdm
import torch.nn as nn
import torch.optim as option
from Models.unet import UNet

#############################################
########### HYPERPARAMETERS #################
LEARNING_RATE = 1e-4
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
BATCH_SIZE = 32
NUM_EPOCHS = 100
NUM_WORKERS = 2
IMAGE_HEIGHT = 160 # 1280 originally
IMAGE_WIDTH = 240  # 1918 originally
PIN_MEMORY = True
LOAD_MODEL = False
DATASET_DIR = "Datasets/downloads/carvana"
TRAIN_IMG_DIR = f"{DATASET_DIR}/train_images/"
TRAIN_MASK_DIR = f"{DATASET_DIR}/train_masks/"
VAL_IMG_DIR = f"{DATASET_DIR}/val_images/"
VAL_MASK_DIR = f"{DATASET_DIR}/val_masks/"

#############################################

