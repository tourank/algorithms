def caesar(string,key):

    encrypted = ""
    for k in string:
        x = ord(k) - 97
        encrypted += chr((x + key) % 26+97)
    return encrypted

string = "xyz"
print(caesar(string,2))
