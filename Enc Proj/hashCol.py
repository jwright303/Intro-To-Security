import sys
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256, SHA1

def weakCol():
  mess = get_random_bytes(8)
  hash_objS = SHA256.new(data=mess)
  dgstS = hash_objS.hexdigest()
  subS = dgstS[:6]
  print(subS)

  count = 0
  while(1):
    count += 1
    mess = get_random_bytes(8)
    hash_obj = SHA256.new(data=mess)
    dgst = hash_obj.hexdigest()
    sub = dgst[:6]
    #print(sub)
    if subS == sub:
      print("Same digest found")
      print(subS, sub)
      print(dgstS, dgst)
      print("count", count)
      break

  print(dgst)
  return 0


def strongCol():
  count = 0
  while(1):
    count += 1
    messA = get_random_bytes(8)
    hash_objA = SHA256.new(data=messA)
    dgstA = hash_objA.hexdigest()
    subA = dgstA[:6]

    messB = get_random_bytes(8)
    hash_objB = SHA256.new(data=messB)
    dgstB = hash_objB.hexdigest()
    subB = dgstB[:6]

    #print(sub)
    if subA == subB:
      print("Same digest found")
      print(subA, subB)
      print(dgstB, dgstA)
      print("count", count)
      break

  return 0


def main():
  choice = sys.argv[1]
  
  if choice == 'w':
    weakCol()
  else:
    strongCol()

  return 0
main()
