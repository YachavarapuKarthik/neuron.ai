import base64

def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        # Read image file and encode to base64
        base64_encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_encoded_image

# Example usage
image_path = "neuronailogo.png"  # Specify your image path here
base64_image = convert_image_to_base64(image_path)

# Print base64 image string (or use it in your email)
print(base64_image)
