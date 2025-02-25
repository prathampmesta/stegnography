import cv2
from IPython.display import display
from PIL import Image

def decrypt_image(image_path):
    img = cv2.imread(image_path)  # Read encrypted image
    if img is None:
        print("Error: Image not found!")
        return

    c = {i: chr(i) for i in range(255)}  # Pixel-to-character mapping

    try:
        with open("password.txt", "r") as f:
            stored_password = f.read().strip()
    except FileNotFoundError:
        print("Error: Password file not found!")
        return

    entered_password = input("Enter passcode for decryption: ")

    if entered_password != stored_password:
        print("YOU ARE NOT AUTHORIZED!")
        return

    n, m, z = 0, 0, 0
    message = ""

    while True:
        try:
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3  # Cycle through RGB channels
        except KeyError:
            break  # Stop if invalid pixel value

    print("Decryption successful! Secret message:", message)

    # Display the encrypted image in Jupyter Notebook for reference
    display(Image.open(image_path))

# Run the decryption function in Jupyter
image_path = "encryptedImage.jpg"
decrypt_image(image_path)