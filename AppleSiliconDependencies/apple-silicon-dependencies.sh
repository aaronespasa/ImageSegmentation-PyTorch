!#/bin/bash

# echo "Creating the venv folder..."
# python3 -m venv ../venv && source ../venv/bin/activate

# brewFolder=$(brew --prefix)

# if [ -d "$brewFolder/hombrew" ]
# then
#     brewFolder="${brewFolder}/homebrew"
# elif [ -d "$brewFolder/Hombrew" ]
# then
#     brewFolder="${brewFolder}/Homebrew"
# else
#     echo "We could not find the HomeBrew folder. Make sure you have installed HomeBrew."
#     exit 0
# fi

# brewCommand="${brewFolder}/bin/brew"
export OPENBLAS=$(brew --prefix openblas)
export CFLAGS="-falign-functions=8 ${CFLAGS}"

pip install wheel
pip install https://github.com/scipy/scipy/releases/download/v1.7.3/scipy-1.7.3-cp39-cp39-macosx_12_0_arm64.whl

