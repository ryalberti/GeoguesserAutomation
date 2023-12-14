from google.cloud import vision
import os 

################################
# language detection and google api key insertion
def detect_language(image_path,json_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_path
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