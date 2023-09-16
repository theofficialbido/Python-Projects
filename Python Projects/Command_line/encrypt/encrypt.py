def machine():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    Value = 'lfeqibspxnmcwvzadojuytrhgk !'

    encryptDict = dict(zip(keys, Value))
    decryptDict = dict(zip(Value, keys))

    message = input("Please enter a Message: ")
    mode = input("Please select an encryption mode : Encode(E) OR Decode(D): ")

    if mode.upper() == 'E':
        newMessage = ''.join([encryptDict[letter]for letter in message.lower()])

    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter]for letter in message.lower()])
    else:
        print('Please enter an Valid choice, Decrypt(D) OR Encrypt(E)')

    return newMessage


print(machine())