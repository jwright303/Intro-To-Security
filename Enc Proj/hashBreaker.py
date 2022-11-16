import sys
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

#This code was gotten from the professor's post in ED Discussion when recommending to print out values to ensure accurate types
def printDetails(plaintext1_bytes, ciphertext_bytes, plaintext2_bytes, key_bytes, iv_bytes):
    print("Plaintext1: '", str(plaintext1_bytes, encoding='utf-8'), "'", sep='')
    print("Ciphertext: ", ''.join(format(x, '02x') for x in ciphertext_bytes), sep='')
    print("Plaintext2: '", str(plaintext2_bytes, encoding='utf-8'), "'", sep='')
    print("Key:        '", str(key_bytes, encoding='utf-8'), "'", sep='')
    print("IV:         ", ''.join(format(x, '02x') for x in iv_bytes), sep='')
    return 0

def main():
  f = open("dict.txt", "r")
  c=0

  pt = b"This is a top secret."
  ct = bytes.fromhex("8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9")
  ct_string = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"

  iv = bytes.fromhex("00000000000000000000000000000000")

  for x in f:
    c += 1
    word = x.rstrip(x[-1])

    if len(word) < 16:
      newW = word.ljust(16)
      key = bytes(newW, "utf-8")
      
      #printDetails(bytes(pt), ct, bytes(pt), key, iv)
      cipher = AES.new(key, AES.MODE_CBC, iv)
      ct_bytes = cipher.encrypt(pad(pt, AES.block_size))
      ct_new = ct_bytes.hex()
      

      if ct_string == ct_new:
        print("key found:", word)
        print("Encrypted message with found key:", ct_new)
        break


  return 0

main()
