from Crypto.Hash import HMAC, SHA1
import sys
import time
import math
import qrcode
from datetime import datetime, timezone, timedelta

def genQr():
  exStr = "otpauth://totp/Me:alice@example.com?secret=HXDMVJECJJWSRB3HWIZR4IFUGFTMXBOZ&issuer=Me&digits=8&period=30"
  img = qrcode.make(exStr)
  img.save("qr.jpg")
  
  return

def genOTP(time, key, real=None):
  #t = datetime.now(timezone.utc).timestamp()
  #t = time.time()
  t = time
  curTime = (math.floor(t/30))
  
  timeStr = str(hex(curTime))[2:]
  while (len(timeStr) < 16):
    timeStr = "0" + timeStr
  
  newMes = bytearray.fromhex(timeStr)
  h = HMAC.new(key, msg=newMes, digestmod=SHA1)
  out = h.digest()

  #Extract the last hex value of the hash (last 4 bits)
  offset = out[len(out)-1] & 0xf
  
  #Use the last 4 bits as the index of the hash
  binary = ((out[offset] & 0x7f) << 24) | ((out[offset + 1] & 0xff) << 16) | ((out[offset + 2] & 0xff) << 8) | (out[offset + 3] & 0xff)
  
  otp = binary % 100000000
  otp = str(otp)
  while len(otp) < 8:
    otp = "0" + otp
  #print(newMes)
  print("otp:", otp[:4], end=" ")
  print(otp[4:], end=" ")
  if real != None:
    real = str(real)
    print("exp:", real[:4], end=" ")
    print(real[4:])
  else:
    print("")
  return

def main():
  argc = len(sys.argv)
  args = sys.argv
 
  if argc < 2:
    print("Not enough arguments provided, program cannot run")
    print("To run the program enter 'python3 submission --generate-qr'")
    print("The program can also be ran with --get-otp in replacement of --generate-qr")
    return -1

  if args[1] == "--generate-qr":
    print("Generating QR code")
    genQr()
  elif args[1] == "--get-otp":
    print("Genearting OTP")
    while(1):
      t = datetime.now(timezone.utc).timestamp()
      key = b"HXDMVJECJJWSRB3HWIZR4IFUGFTMXBOZ"
      genOTP(t, key)
      time.sleep(30)
  elif args[1] == "val":
    print("Validating algorithm - generated otp, expected otp")
    tims = [59, 1111111109, 1111111111, 1234567890, 2000000000, 20000000000]
    otps = [94287082, "07081804", 14050471, 89005924, 69279037, 65353130]
    key = b"12345678901234567890"

    for i in range(0, len(tims)):
      genOTP(tims[i], key, otps[i])

  return 0

main()
