"""
Implementation of the U-Net model architecture.

Copyright (c), Aarón Espasandín - All Rights Reserved

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree:
https://github.com/aaronespasa/ImageSegmentation-PyTorch/blob/main/LICENSE
"""
import torch
import torch.nn as nn
from torch.nn.modules import module
import torchvision.transforms.functional as TF

class DoubleConvolution(nn.Module):
    def __init__(self, in_channels: int, out_channels: int):
        super(DoubleConvolution, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),

            nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
        )
    
    def forward(self, x):
        return self.conv(x)

class UNet(nn.Module):
    """UNet model implementation for image segmentation """
    def __init__(self, in_channels:int = 3, out_channels:int = 2, features:list = [64, 128, 256, 512]):
        """
        Args:
            in_channels (int): Number of channels of each input image.
                                    - For RGB images: in_channels = 3
                                    - For B&W images: in_channels = 1
            out_channels (int): Number of different classes our model is segmenting. 
                                    - For binary segmentation (background & car): out_channels = 2
            features (int list): Number of features ("out_channels") that will have 
                                 each Double Convolution.
                                    - Example: features = [64, 128, 256]

        """
        super(UNet, self).__init__()
        self.features = features
        self.in_channels = in_channels

        self.ups = self.create_increasing_layers()
        self.downs = self.create_decreasing_layers()

        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
    
    def create_decreasing_layers(self, moduleList = nn.ModuleList()):
        """"Create the decreasing part of the UNet model architecture"""
        in_channels = self.in_channels

        for feature in self.features:
            moduleList.append(DoubleConvolution(in_channels, feature))
            # Actual num. of input channels == previous num. of output channels
            in_channels = feature

        return moduleList
    
    def create_increasing_layers(self, moduleList = nn.ModuleList()):
        """Create the increasing part of the UNet model architecture"""

