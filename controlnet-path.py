from cryptography.fernet import Fernet

def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message
def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message.decode()
message = "webui"
key = Fernet.generate_key()

command_path = f"sd-{decrypted_message}-controlnet"
print("Command Path:", command_path)
