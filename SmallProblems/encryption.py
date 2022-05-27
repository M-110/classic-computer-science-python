from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    """Generate a random key of given length"""
    random_bytes: bytes = token_bytes(length)
    return int.from_bytes(random_bytes, byteorder="big")


def encrypt(data: str) -> Tuple[int, int]:
    """Encrypt a string, returning the key and the encrypted data"""
    data_as_bytes: bytes = data.encode()
    encryption_key: int = random_key(len(data_as_bytes))
    data_key: int = int.from_bytes(data_as_bytes, byteorder="big")
    
    encrypted_data: int = data_key ^ encryption_key
    
    return encryption_key, encrypted_data


def decrypt(encrypted_data: int, encryption_key: int) -> str:
    """Decrypt data back into the original string using the key"""
    data_key: int = encrypted_data ^ encryption_key
    data_as_bytes: bytes = data_key.to_bytes((data_key.bit_length() + 7) // 8, byteorder="big")
    data: str = data_as_bytes.decode()
    return data


if __name__ == "__main__":
    original_data = "Hello, Secret World!"
    print(f'Original data to be encrypted: {original_data!r}')
    
    my_key, my_encrypted_data = encrypt(original_data)
    print(f'\nData after encryption: {my_encrypted_data}')
    print(f'My secret key: {my_key}')
    
    decrypted_data = decrypt(my_encrypted_data, my_key)
    print(f'\nDecrypted data using the secret key: {decrypted_data!r}')
