import sys
#from Crypto.Random import get_random_bytes
#from Crypto.Hash import SHA256, SHA1, SHA512, MD5, MD2, SHA224, SHA384, SHA3_224, SHA3_256, SHA3_384, SHA3_512
from bitarray import bitarray
import mmh3

siz = 2000000
k = 14

def buildBF():
  f = open("dictionary.txt", encoding="ISO-8859-1")
  #byteWord = bytes(word, 'utf-8')

  #siz = 5000000
  #bloomF = [0] * siz
  bloomF = bitarray(siz)
  bloomF.setall(0)
  print(siz)

  for x in f:
    #print(x)
    mess = bytes(x, "ISO-8859-1")
    for i in range(0, k):
      ind = mmh3.hash(mess, i) % siz
      #ind = hashSwitch(i, mess)
      bloomF[ind] = 1


  #print(bloomF)
  f.close()

  return bloomF

def getIndecies(word):
  #siz = 5000000

  mess = bytes(word, 'utf-8')
  indxs = []
  for i in range(0, k):
    #ind = hashSwitch(i, mess)
    ind = mmh3.hash(mess, i) % siz
    indxs.append(ind)
  #indxs = [i1, i2, i3, i4]

  return indxs

def main():
  print("Creating bloom filter...")
  bf = buildBF()
  print("Finished building bloom filteri\n")


  choice = input("Enter f to have program read from a file or u to have it read from the user in the command line: ")
  if (choice == "f"):
    print("file read")
    inFile = open("sample_input.txt", "r")

    for line in inFile:
      newL = line[:-1]
      inds = getIndecies(line)

      res = []
      for ind in inds:
        res.append(bf[ind])
      #print(res)
      #print(line, inds)
      #if bf[inds[0]] == 1 and bf[inds[1]] == 1 and bf[inds[2]] == 1 and bf[inds[3]] == 1:
      if 0 in res:
        print(newL + ": \t\t\tfine password")
      else:
        print(newL + ": \t\t\tmaybe bad password")

  elif (choice == "u"):
    print("command line read")
    while True:
      word = input("Enter the password to check or stop to stop: ")
      if word == "stop":
        break
      else:
        inds = getIndecies(word)
        res = []
        for ind in inds:
          res.append(bf[ind])
        if 0 in res:
          print(word + ": \t\t\tfine password")
        else:
          print(word + ": \t\t\tmaybe bad password")

  else:
    print("invalid input program quiting (enter 'u' or 'f')")
    return -1

  return 0

main()
