# this is the program that gets run to hold all the other ones
# to call: python geoguess.py <image.jpg> 

#####################################
# imports
import os 
import argparse
import aggregatecode as agc
import language_det as ladet
from arch_classification.vgg_classify import arch_classify
from License_Plate_Detection.license_det import license_det

#####################################
# define locations and var names 

dir_path = os.getcwd()
loc_path = dir_path + "\\locations\\"
json_path = dir_path + "\\geoguesserautomation-5264cd87ce70.json"
arch_path = dir_path + "\\arch_classification\\"
mlb_path = arch_path + "mlb.pickle"
arch_model = arch_path + "arch_model.pkl"


#####################################
# define functions 

def parse_args():
    parser = argparse.ArgumentParser(
        prog = 'Geoguesser Automation',
        description='Automatically detects image characteristics without metadata. \nusage: geoguess.py <img.jpg>'
    )
    parser.add_argument("file")
    args = parser.parse_args()
    if not args.file:
        print("file input required.")
        quit()
    return args.file

def process_license(input):
    # will call the necessary parts of the license plate functions 
    # returns list of license plates (or an empty list) 
    ret = license_det(input)
    print("License plate function")
    print("License plate: " + ret)
    return ret

def process_language(image_path):
    print("Language detection")
    detected_language = ladet.detect_language(image_path,json_path)
    print(f"Detected language: {detected_language}")
    ret = []
    return detected_language 

def process_architecture(image_path,model,labelbin):
    # will call architecture functions 
    # will return list of arch characteristics
    ret = arch_classify(image_path,model,labelbin)
    print("architecture")
    return ret 

#####################################
# main function

def main():
    print("Geoguesser Automation: \nDetecting image location without metadata based on architecture, license plates, and language")
    input = parse_args() #  "image_input.jpg"
    print("Classifying " + input)
    
    allLoc = agc.loadLocs(loc_path)

    # TODO: fill these in as the models are completed. 
    license_output = process_license(input)
    language_ouput = process_language(input,json_path)
    arch_output = process_architecture(input,arch_model,mlb_path)

    print(agc.process_tags(allLoc,(license_output,language_ouput,arch_output)))


main()