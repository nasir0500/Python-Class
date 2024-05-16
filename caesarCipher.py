#caesar cipher Encryption and decryption
def substitution(message, key):
  shiftedMessage = ""
  for latter in message:
    if latter.isupper():
      shiftedMessage += chr((ord(latter)+key-65) % 26 + 65)
    elif latter.islower():
      shiftedMessage += chr((ord(latter)+key-97) % 26 + 97)
    else:
      continue #if space needed: shiftedMessage += latter
  return shiftedMessage

M = input("Enter the message: ")
K = int(input("Enter the key fo shifting: "))
encrypted = substitution(M, K)
decrypted = substitution(encrypted, -1*K)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
