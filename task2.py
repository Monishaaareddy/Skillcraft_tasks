from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            
            
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

 
input_image = r"C:\Users\pandurangavital maha\OneDrive\Desktop\portfolio\input.jpg"
encrypted_image = r"C:\Users\pandurangavital maha\OneDrive\Desktop\project\encrypted_image.jng.bmp"
decrypted_image = r"C:\Users\pandurangavital maha\OneDrive\Desktop\project\decrypted_image.jpg.bmp"
encrypt_image(input_image, encrypted_image, key=None)


decrypt_image(encrypted_image, decrypted_image, key=None)
