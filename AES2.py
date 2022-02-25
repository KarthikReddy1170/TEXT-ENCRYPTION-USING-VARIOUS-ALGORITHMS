from Cryptodome.Cipher import AES
from secrets import token_bytes

key =token_bytes(16)

def encrypt(msg):
    cipher=AES.new(key,AES.MODE_EAX)
    nonce=cipher.nonce
    ciphertext, tag=cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce,ciphertext,tag

def decrypt(nonce,ciphertext,tag):
    cipher=AES.new(key,AES.MODE_EAX,nonce=nonce)
    text=cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return text.decode('ascii')
    except:
        return False


nonce,ciphertext,tags=encrypt('AES USE A MATRIX')
text=decrypt(nonce,ciphertext,tags)
print(f'Cipher text: {ciphertext}')
if not text:
    print('message is corrupted')
else:
    print(f'text: {text}')