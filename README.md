# Learn image segmentation using PyTorch

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