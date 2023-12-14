# Holds aggregate functions to be called on by geoguess.py 

#####################################
# imports 
import os 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/danaj/Desktop/EE462finalproject/ee462finalproject-3e96cda81771.json"
from google.cloud import vision
import pickle
# import location_class

#####################################
# define functions 

# Function to prioritize tags based on weight
def prioritize_tags(location):
    sorted_tags = sorted(location.tags, key=lambda x: x[1], reverse=True)
    return [tag[0] for tag in sorted_tags]



def process_tags(allLoc,foundChara):
    # returns best match 
    # foundChara = license_output, language_ouput, arch_output
    possible = "Unknown location"
    bestPoints=0
    for thisLoc in allLoc:
        locPoints=0
        locTags = thisLoc.get_tags()
        for header in foundChara:
            for thisChara in header:
                if (thisChara in locTags.keys()):
                    locPoints += locTags[thisChara]
        if (locPoints>=bestPoints):
            possible = thisLoc
            bestPoints = locPoints
        
    # TODO: maybe just loop thru a few pre determined objects 
    return possible

# Call the function to process user input
# process_input()

def loadLocs(loc_path):
    # loading all the pickles of each location to a list of objects
    # returns list of locations 
    print("Loading locations")
    allLoc = []
    locs_list = os.listdir(loc_path)
    for eachloc in locs_list:
        thisLoc = pickle.load(loc_path+"\\" + eachloc) # should be a Location obj 
        allLoc.append(thisLoc)
        print(thisLoc.name)

    return allLoc

################################
# language detection and google api key insertion
def detect_language(image_path):
    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Assuming the first detected text contains the language information
    if texts:
        detected_text = texts[0].description
        # You can use a language detection library here or implement your own logic
        # For simplicity, let's assume that the first word in the detected text is the language
        detected_language = detected_text.split()[0]
        return detected_language
    else:
        return "Unknown"

######################################################
# Usage with photo of stevens from my computer

image_path = "C:/Users/danaj/Desktop/EE462finalproject/AERIAL_STEVENS_INSTITUTE_40-crop2.jpg"
detected_language = detect_language(image_path)
print(f"Detected language: {detected_language}")

############################################################
# Everything below this are things I don't think we need but I didn't think we should delete yet 

# # Function to process license plate information
# def process_license_plate(license_plate):
#     location = Location("Unknown")
#     if license_plate:
#         location.add_tag("License Plate", 2)
#     return location

# # Function to process language information
# def process_language(language):
#     location = Location("Unknown")
#     if language:
#         location.add_tag(language, 1)
#     return location

# # Function to process architecture information
# def process_architecture(architecture):
#     location = Location("Unknown")
#     if architecture:
#         location.add_tag(architecture, 3)
#     return location
# Function to process user input and print prioritized tags

# def process_input():
#     # Get user input
#     license_plate = input("Enter license plate information (or press Enter to skip): ")
#     language = input("Enter language information (or press Enter to skip): ")
#     architecture = input("Enter architecture information (or press Enter to skip): ")

#     # Process each type of information
#     location_license_plate = process_license_plate(license_plate)
#     location_language = process_language(language)
#     location_architecture = process_architecture(architecture)

#     # Combine tags from all sources
#     combined_tags = (
#         location_license_plate.tags +
#         location_language.tags +
#         location_architecture.tags
#     )

#     # Create a new location and add combined tags
#     combined_location = Location("Combined")
#     combined_location.tags = combined_tags

#     # Prioritize and print tags
#     prioritized_tags = prioritize_tags(combined_location)
#     print(f"Location: {combined_location.name}\nTags: {', '.join(prioritized_tags)}")
