from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)
buffer_size = 65536
def PutKey():
    file_in = open("key_location.txt", 'wb')
    key_from_file = file_in.write(key)
    file_in.close()
    return key_from_file

def ImgEncryption():
    file_to_encrypt = input("Input the file to encrypt : ")
    # open the input and output files in binary format
    inFile = open(file_to_encrypt, 'rb')
    outFile = open('encrypted_' + file_to_encrypt, 'wb')

    # create cipher object and encrypt
    cipher = AES.new(key, AES.MODE_CFB) #auto generates iv
    PutKey()

    # write the iv to the output file
    outFile.write(cipher.iv)

    # keep reading the file into the buffer, encrypting then writing to the new file
    buffer = inFile.read(buffer_size)
    while len(buffer) > 0:
        cipher_data = cipher.encrypt(buffer)
        outFile.write(cipher_data)
        buffer = inFile.read(buffer_size)

    # close the files
    inFile.close()
    outFile.close()