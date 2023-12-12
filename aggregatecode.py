class Location:
    def __init__(self, name):
        self.name = name
        self.tags = []

    def add_tag(self, tag, weight=1):
        self.tags.append((tag, weight))

# Sample locations
tokyo = Location("Tokyo")
paris = Location("Paris")

# Sample tagging
tokyo.add_tag("City", 2)
tokyo.add_tag("Skyscrapers", 3)
tokyo.add_tag("Japanese Text", 1)

paris.add_tag("City", 2)
paris.add_tag("French Language", 2)
paris.add_tag("French Architecture", 3)

# Function to prioritize tags based on weight
def prioritize_tags(location):
    sorted_tags = sorted(location.tags, key=lambda x: x[1], reverse=True)
    return [tag[0] for tag in sorted_tags]

# Function to process the input from the models
def process_input(license_plate, language, architecture):
    # Create a location object based on the available information
    location = Location("Unknown")

    # Add tags based on the inputs
    if license_plate:
        location.add_tag("License Plate", 2)
    if language:
        location.add_tag(language, 1)
    if architecture:
        location.add_tag(architecture, 3)

    # Prioritize and print tags
    prioritized_tags = prioritize_tags(location)
    print(f"Location: {location.name}\nTags: {', '.join(prioritized_tags)}")

# Sample input
process_input("ABC123", "Japanese", "Izba")
