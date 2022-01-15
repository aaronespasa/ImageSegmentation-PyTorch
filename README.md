# Learn image segmentation using PyTorch

First, I recommend to read the notebook **main-techniques.ipynb**. 

There you will learn about upsampling methods (simple scaling and transposed convolutions), skip connections, evalution (IoU and Dice Score) and other useful techniques used in the field of image segmentation.

## Image Segmentation models:
- [ ] Fully Convolutional Networks (SegNet)
- [ ] FCN-32, FCN-16, FCN-8
- [x] U-Net
- [ ] Mobile UNet
- [ ] Mask R-CNN
- [ ] PSPNet: Pyramid Scene Parsing Network
- [ ] BiSeNet: Bilateral Segmentation Network (real-time)
- [ ] DeepLabV3+
- [ ] Segmenter: Vision transformers applied to semantic image segmentation.

## Requirements
> I encourage you to have a version of Python greater than the version 3.9.0 but lower
> than the version 3.9.9 to avoid having incompatibility issues with dependencies like
> torchvision. Otherwise, you may experiment some issues installing the latest version
> of the dependencies <- `python3` should use this version

## Setup

Create a virtual environment and activate it:
```bash
$ python3 -m venv ./venv && source ./venv/bin/activate
```

### If you're using Apple Silicon, execute the following command
⚠️ Make sure your terminal is not using Rosetta and you're using MacOS 12!

The following command will install scipy to avoid dependency problems:
```
$ cd AppleSiliconDependencies && bash apple-silicon-dependencies.sh
$ cd ..
```

## Install the dependencies

Install the Python requirements:
```bash
$ pip install -r requirements.txt
```
