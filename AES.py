from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

data=b"SECRETDATA"
key = get_random_bytes(16) #must be 16, 24 or 32 bytes long
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("encrypt.txt", "bw")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()

file_in = open("encrypt.txt", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]


cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data.decode('UTF-8'))