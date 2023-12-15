# Info
## Goal:
Identify location of photograph by identifying license plates, language of pictured signs, and architecture without image metadata. This will be done using a series of automated systems.
Runs on python 3.7.16
## Usage
1. This project requires two environments. All are installed in Anaconda. The first environment is used to train the detection model for the license plate detection. Jupyter Notebook is required to run license plate detection.

```
git clone git@github.com:ryalberti/GeoguesserAutomation.git
2. Prepare the license plate detector
```
cd GeoguesserAutomation
cd License_Plate_Detection
conda create -n licenseenv python=3.11
conda activate licenseenv
conda install -c anaconda pip
pip install opencv-python
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install easyocr
pip install imutils
pip install matplotlib
pip install ipykernel
```
After installing all the packages, you need to link an jupyter notebook kernel to your virtual environment:
```
python -m ipykernel install --name=licenseenv
```
Now that the kernel is linked, download the ANPR OpenCV.ipynb file and open it within Jupyter Notebook. Make sure when you open the file, that the licenseenv kernel is selected. Then use Shift+Enter to go cell by cell until the end where the license plate detection is done.

3. The second is for training the architecture model.

```
conda deactivate
conda create -n archenv python=3.7 
conda activate archenv
conda install -c anaconda pip
pip install imutils 
pip install matplotlib
pip install opencv-python
pip install scikit-learn
pip install tensorflow
```
4. Train the architecture model.
```
cd arch_classification
python vgg_Train.py 
```
5. Place your API key into the file. Paste in your key, save, quit.
```
notepad geoguesserautomation-5264cd87ce70.json
```

6. Run the script
```
python geoguess.py test_images/test1.png
```
