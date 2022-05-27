from encryption import random_key


def encrypt_image(file_name: str) -> int:
    """Encrypt image as a new file.
    
    The new file will be the original file name + '_encrypted.jpg'
    
    Returns the encryption key.
    """
    with open(file_name + '.jpg', 'rb') as image:
        data: bytes = image.read()

    encryption_key: int = random_key(len(data))
    data_key: int = int.from_bytes(data, byteorder="big")

    encrypted_data: int = data_key ^ encryption_key
    encrypted_data_as_bytes: bytes = encrypted_data.to_bytes(
        (encrypted_data.bit_length() + 7) // 8, 'big')
    with open(file_name + '_encrypted.jpg', 'wb') as image_out:
        image_out.write(encrypted_data_as_bytes)
    print(f'Saved encrypted image as "{file_name}_encrypted.jpg"')
    return encryption_key


def decrypt_image(file_name: str, encryption_key: int):
    """Decrypt an image and save it with the '_decrypted' affix."""
    with open(file_name + '_encrypted.jpg', 'rb') as image:
        encrypted_data: bytes = image.read()
    encrypted_data_as_int: int = int.from_bytes(encrypted_data, 'big')
    data_key: int = encrypted_data_as_int ^ encryption_key
    data_as_bytes: bytes = data_key.to_bytes((data_key.bit_length() + 7) // 8, byteorder="big")

    with open(file_name + '_decrypted.jpg', 'wb') as image_out:
        image_out.write(data_as_bytes)
    print(f'Saved decrypted image as "{file_name}_decrypted.jpg"')


if __name__ == "__main__":
    file_name = 'original_image'
    key = encrypt_image(file_name)
    decrypt_image(file_name, key)
