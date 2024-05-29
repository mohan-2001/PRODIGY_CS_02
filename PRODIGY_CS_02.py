from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to a numpy array
    image_array = np.array(image)

    # Perform the encryption operation
    encrypted_array = image_array ^ key

    # Convert the encrypted array back to an image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))

    # Save the encrypted image
    encrypted_image.save('encrypted_image.png')
    return

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)

    # Convert the encrypted image to a numpy array
    encrypted_array = np.array(encrypted_image)

    # Perform the decryption operation
    decrypted_array = encrypted_array ^ key

    # Convert the decrypted array back to an image
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))

    # Save the decrypted image
    decrypted_image.save('decrypted_image.png')
    return

image_path = 'Prodigyinfotech.jpeg'
key = 0x1476586578656 
encrypt_image(image_path, key)
decrypt_image('encrypted_image.png', key)