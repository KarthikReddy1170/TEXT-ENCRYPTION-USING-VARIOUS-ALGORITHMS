sharedPrime=int(input())
sharedBase=int(input())
aliceSecret=int(input())
bobSecret=int(input())
# Begin
print("Publicly Shared Variables:")
print("    Publicly Shared Prime: ", sharedPrime)
print("    Publicly Shared Base:  ", sharedBase)
# Alice Sends Bob A = g^a mod p
A = (sharedBase ** aliceSecret) % sharedPrime
print("\n  Alice Sends Over Public Chanel: ", A)
# Bob Sends Alice B = g^b mod p
B = (sharedBase ** bobSecret) % sharedPrime
print("\n  Bob Sends Over Public Chanel: ", B)
print("\n------------\n")
print("Privately Calculated Shared Secret:")
# Alice Computes Shared Secret: s = B^a mod p
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print("    Alice Shared Secret: ", aliceSharedSecret)

# Bob Computes Shared Secret: s = A^b mod p
bobSharedSecret = (A ** bobSecret) % sharedPrime
print("    Bob Shared Secret: ", bobSharedSecret)