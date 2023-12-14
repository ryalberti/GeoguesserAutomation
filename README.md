# Info
## Goal:
Identify location of photograph by identifying license plates, language of pictured signs, and architecture without image metadata. This will be done using a series of automated systems.
Runs on python 3.7.16
## Usage
1. This project requires two environments. All are installed in Anaconda. The first environment is used to train the detection model for the license plate detection.

```
git clone git@github.com:ryalberti/GeoguesserAutomation.git
conda create -n licenseenv python=3.11.7
```
2. The second is for training the architecture model.

```
conda deactivate
conda create -n archenv python=3.7 
conda activate archenv
conda install -c anaconda pip
pip install keras
Pip install pandas
pip uninstall keras-preprocessing
pip install git+https://github.com/keras-team/keras-preprocessing.git
pip install tensorflow
pip install pillow
python -m pip install scipy
pip install google-cloud-vision
cd arch_classification
```
