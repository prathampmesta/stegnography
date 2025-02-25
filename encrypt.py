import cv2
import numpy as np
from IPython.display import display
from PIL import Image

def encrypt_image(image_path, output_path, message, password):
    img = cv2.imread(image_path)  # Read image
    if img is None:
        print("Error: Image not found!")
        return

    d = {chr(i): i for i in range(255)}  # Character-to-pixel  

    n, m, z = 0, 0, 0

    for char in message:
        img[n, m, z] = d[char]  # Store ASCII values in pixels
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through RGB channels

    cv2.imwrite(output_path, img)  # Save encrypted image
    print(f"Encryption successful! Encrypted image saved as {output_path}") 

    with open("password.txt", "w") as f:
        f.write(password)  # Save password in a file

    # Display encrypted image in Jupyter Notebook
    display(Image.open(output_path))

# Run the encryption function in Jupyter
image_path = "abc.jpg"  # Replace with the correct image path
output_path = "encryptedImage.jpg"

message = input("Enter secret message: ")
password = input("Enter a passcode: ")

encrypt_image(image_path, output_path, message, password)