import pickle
import os
import aggregatecode as agc

dir_path = os.getcwd()
loc_path = dir_path + "\\locations"

print("For adding locations and their tags")

running = True

def clean_input(input):
    # input = "aframe,1"
    # return = ("aframe",1) which is a tuple, 1 is an int 
    input_array = input.lower().split(",")
    return (input_array[0],int(input_array[1]))

def weighting(header):
    # Header = license plate, language, arch
    ret =[] # list of tuples 
    while True:
        tag = input("Enter the " + header + " and the weight separated by a comma. When done, press ENTER. \nEX. city,4\n")
        if not tag:
            break
        tag = clean_input(tag)
        ret.append((tag[0],tag[1]))
    return ret

while running:
    # Get user input
    location_name = input("enter the name of the place: ")
    # license_plate = input("Enter license plate information (or press Enter to skip). No spaces, only commas: ")
    location_license_plate = weighting("license plate")
    # language = input("Enter language information (or press Enter to skip) No spaces, only commas: ")
    location_language = weighting("language")
    # architecture = input("Enter architecture information (or press Enter to skip) No spaces, only commas: ")
    location_architecture = weighting("architecture")

    # Process each type of information
    location_name = location_name.lower()
    # location_license_plate = clean_input(license_plate)
    # location_language = clean_input(language)
    # location_architecture = clean_input(architecture)

    newLoc = agc.Location(location_name, location_language, location_license_plate,location_architecture)
    with open(location_name+".pkl", 'wb') as file:
        pickle.dump(newLoc,file)

    # Combine tags from all sources
    combined_tags = (
        location_license_plate.tags +
        location_language.tags +
        location_architecture.tags
    )