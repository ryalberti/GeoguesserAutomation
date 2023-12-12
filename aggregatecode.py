class Location:
    def __init__(self, name):
        self.name = name
        self.tags = []

    def add_tag(self, tag, weight=1):
        self.tags.append((tag, weight))

# Function to prioritize tags based on weight
def prioritize_tags(location):
    sorted_tags = sorted(location.tags, key=lambda x: x[1], reverse=True)
    return [tag[0] for tag in sorted_tags]

# Function to process license plate information
def process_license_plate(license_plate):
    location = Location("Unknown")
    if license_plate:
        location.add_tag("License Plate", 2)
    return location

# Function to process language information
def process_language(language):
    location = Location("Unknown")
    if language:
        location.add_tag(language, 1)
    return location

# Function to process architecture information
def process_architecture(architecture):
    location = Location("Unknown")
    if architecture:
        location.add_tag(architecture, 3)
    return location

# Function to process user input and print prioritized tags
def process_input():
    # Get user input
    license_plate = input("Enter license plate information (or press Enter to skip): ")
    language = input("Enter language information (or press Enter to skip): ")
    architecture = input("Enter architecture information (or press Enter to skip): ")

    # Process each type of information
    location_license_plate = process_license_plate(license_plate)
    location_language = process_language(language)
    location_architecture = process_architecture(architecture)

    # Combine tags from all sources
    combined_tags = (
        location_license_plate.tags +
        location_language.tags +
        location_architecture.tags
    )

    # Create a new location and add combined tags
    combined_location = Location("Combined")
    combined_location.tags = combined_tags

    # Prioritize and print tags
    prioritized_tags = prioritize_tags(combined_location)
    print(f"Location: {combined_location.name}\nTags: {', '.join(prioritized_tags)}")

# Call the function to process user input
process_input()
