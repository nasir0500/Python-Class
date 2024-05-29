#Hill cipher with numpy
import numpy as np
def filler(text):
    letters = ['z', 'x', 'q']
    for letter in letters:
        if letter not in text:
            filer = letter
            return filer
            break

def textToMatrix(text):
    row = int(len(text)/3)
    mat = [[0]*3 for i in range(row)]
    k = 0
    for r in range(row):
        for c in range(3):
            mat[r][c] = (ord(text[k])-97)%26
            k += 1
    return mat

def matrixToText(mat):
    text = ''
    row = len(mat)
    for r in range(row):
        for c in range(3):
            text += chr(mat[r][c]+97)
    return text

def encryption(messageMatrix, key):
    cipherMatrix = np.mod(np.dot(messageMatrix, key), 26)
    return cipherMatrix


def decryption(ciphertextMatrix, key):
    det = np.linalg.det(key)
    invMat = np.linalg.inv(key)
    adjMat = np.round(np.mod(invMat*det, 26))
    adjMat[adjMat == 26.] = 0
    adjMat = adjMat.astype(int)
    #p = (c*k^-1)mod26
    det = det % 26
    for i in range(26):
        if (i*det)%26 == 1:
            multiplicativeInverse = i
    p = np.dot(ciphertextMatrix, adjMat)
    plaintextMatrix = np.mod(np.multiply(multiplicativeInverse, p), 26)
    return plaintextMatrix

message = "Pay more money".lower().replace(" ","")
key = [
        [17, 17, 5],
        [21, 18, 21],
        [2, 2, 19]
    ]

fil = filler(message)
if len(message) % 3 == 0:
    message = message
elif len(message) % 3 == 2:
    message = message + fil
else:
    message = message + fil + fil

if isinstance(key, list):
    key = key
else:
    key = textToMatrix(key.lower().replace(" ",""))

message = textToMatrix(message)
encryptedMatrix = encryption(message, key)
ciphertext = matrixToText(encryptedMatrix)
decryptedMatrix = decryption(encryptedMatrix, key)
plaintext = matrixToText(decryptedMatrix).replace(fil, "")
print("ciphertext:", ciphertext)
print("decrypted text:",plaintext)
