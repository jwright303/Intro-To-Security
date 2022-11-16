To run this program, enter "python3 submission.py [param]"
where [param] is replaced by --generate-qr, --get-otp, or val
Note that I added the val parameter to check the program against the TOTP Table 
which was given in the RFC document linked on the assignemnt page.

My version of the TOTP uses a dummy email alice@example.com, the SHA1 hash algorithm, and 8 digits for the otp
The program starts by creating a hash with the given key and the timestamp from when the algorithm was executed
Before this hash is generated, the key to be at least length 16 (this is a hex string so each charachter is 4 bits)
the key of length 16 corresponds to 8 bytes which is the requirement according to the RFC document
Next, the last 4 bits of the hash are used as the index of the hash to use as the otp.
Finally the result is modulated by 10^8 to produce the otp
