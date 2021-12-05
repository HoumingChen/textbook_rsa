import rsa

print("Generate keys:")
public_key, private_key, n = rsa.generate_keys()
print(f"public key: {public_key}")
print(f"private key: {private_key}")
print(f"n: {n}\n\n")

text = 123456789
print(f"Encrypting text {text}:")
ciphertext = rsa.encrypt(text, public_key, n)
print(f"ciphertext {ciphertext}:\n\n")

print(f"Decrypting text {ciphertext}:")
decrypted_text = rsa.decrypt(ciphertext, private_key, n)
print(f"Original text {decrypted_text}\n\n")