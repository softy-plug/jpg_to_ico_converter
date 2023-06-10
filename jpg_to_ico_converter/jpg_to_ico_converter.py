import os
from PIL import Image

def convert_image(input_path, output_folder):
    with Image.open(input_path) as im:
        png_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".png")
        im.save(png_path, format="PNG", quality=100)
        ico_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".ico")
        with Image.open(png_path) as f:
            f.save(ico_path)

def main():
    print("Welcome to JPG to PNG Converter!")
    while True:
        jpg_folder = input("Enter the path to the folder containing JPG images: ")
        if os.path.exists(jpg_folder):
            break
        else:
            print("The folder does not exist.")
    while True:
        ico_folder = input("Enter the path to the folder where converted ICO images will be saved: ")
        if os.path.exists(ico_folder):
            break
        else:
            print("The folder does not exist.")
    # Create the ICO folder if it doesn't exist yet
    if not os.path.exists(ico_folder):
        os.makedirs(ico_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            convert_image(input_path, ico_folder)
    print("All images converted successfully to PNG format and saved as ICO files in the chosen folder!")

if __name__ == "__main__":
    main()

# softy_plug