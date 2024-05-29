#playfair cipher encryption and decryption
def filler(text):
    letters = ['z', 'x', 'q']
    for letter in letters:
        if letter not in text:
            filer = letter
            return filer
            break

def removeMatch(text, fil):
    length = len(text)
    if length % 2 == 0:
        for i in range(0, length, 2):
            if text[i] == text[i + 1]:
                textWithoutMatch = text[0:i + 1] + fil + text[i + 1:]
                textWithoutMatch = removeMatch(textWithoutMatch, fil)
                break
            else:
                textWithoutMatch = text
    else:
        for i in range(0, length - 1, 2):
            if text[i] == text[i + 1]:
                textWithoutMatch = text[0:i + 1] + fil + text[i + 1:]
                textWithoutMatch = removeMatch(textWithoutMatch, fil)
                break
            else:
                textWithoutMatch = text
    return textWithoutMatch


def matrix(key):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    keySquare = ""
    for letter in key + alphabet:
        if letter not in keySquare:
            keySquare += letter
    return keySquare


def diagraph(message):
    return [message[i:i + 2] for i in range(0, len(message), 2)]


def encrypt(diagraphs, keyMatrix):
    result = ""
    for diagraph in diagraphs:
        a, b = diagraph
        rowOfa, colOfa = divmod(keyMatrix.index(a), 5)
        rowOfb, colOfb = divmod(keyMatrix.index(b), 5)

        if rowOfa == rowOfb:
            colOfa = (colOfa + 1) % 5
            colOfb = (colOfb + 1) % 5
        elif colOfa == colOfb:
            rowOfa = (rowOfa + 1) % 5
            rowOfb = (rowOfb + 1) % 5
        else:
            colOfa, colOfb = colOfb, colOfa

        result += keyMatrix[rowOfa * 5 + colOfa] + keyMatrix[rowOfb * 5 + colOfb]
    return result


def decrypt(diagraphs, keyMatrix):
    result = ""
    for diagraph in diagraphs:
        a, b = diagraph
        rowOfa, colOfa = divmod(keyMatrix.index(a), 5)
        rowOfb, colOfb = divmod(keyMatrix.index(b), 5)

        if rowOfa == rowOfb:
            colOfa = (colOfa - 1) % 5
            colOfb = (colOfb - 1) % 5
        elif colOfa == colOfb:
            rowOfa = (rowOfa - 1) % 5
            rowOfb = (rowOfb - 1) % 5
        else:
            colOfa, colOfb = colOfb, colOfa

        result += keyMatrix[rowOfa * 5 + colOfa] + keyMatrix[rowOfb * 5 + colOfb]
    return result


m = input("Enter your text: ").lower().replace(" ", "")
k = 'monarchy'.lower().replace(' ', "")
rep = m.replace("j", "i")
fil = filler(rep)
message = removeMatch(rep, fil)
key = removeMatch(k.replace("j", "i"),fil)
keyMatrix = matrix(key)
if len(message) % 2 == 1:
    message += fil
endiagraphs = diagraph(message)

encrypted = encrypt(endiagraphs, keyMatrix)
decrypted = decrypt(diagraph(encrypted), keyMatrix).replace(fil, "")
print("The plaintext is:", m)
print("The key is:", k)
print("The encrypted text is:", encrypted)
print("The decrypted text is:", decrypted)
