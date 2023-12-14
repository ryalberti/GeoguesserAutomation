# this is the program that gets run to hold all the other ones
# to call: python geoguess.py <image.jpg> 

#####################################
# imports
import os 
import argparse
import aggregatecode as agc
import language_detection

#####################################
# define locations and var names 

dir_path = os.getcwd()
loc_path = dir_path + "\\locations"
language_path = dir_path+"\\language_detection"
json_path = language_path + "ee462finalproject-3e96cda81771.json"


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
    return args

def process_license(input):
    # will call the necessary parts of the license plate functions 
    # returns list of license plates (or an empty list) 
    ret = []
    print("License plate function")
    return ret

def process_language(image_path):
    print("Language detection",json_path)
    detected_language = language_detection.detect_language(image_path)
    print(f"Detected language: {detected_language}")
    ret = []
    return detected_language 

def process_architecture(input):
    # will call architecture functions 
    # will return list of arch characteristics
    ret = []
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
    language_ouput = process_language(input)
    arch_output = process_architecture(input)

    print(agc.process_tags(allLoc,(license_output,language_ouput,arch_output)))





