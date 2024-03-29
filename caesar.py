def main():
    action = input("1. Encryption\n2. Decryption\nChoose (1/2): ")

    def encrypt(text, key):
        result = ''
        for i in range(len(text)):
            char = text[i]
            if (char.isupper()):
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif (char.islower()):
                result += chr((ord(char) + key - 97) % 26 + 97)
            elif char == '':
                result += ''
        return result

    def decrypt(text,key):
        result = ''
        for i in range(len(text)):
            char = text[i]
            if (char.isupper()):
                result += chr((ord(char) - key - 65) % 26 + 65)
            elif (char.islower()):
                result += chr((ord(char) - key - 97) % 26 + 97)
            elif char == '':
                result += ''
        return result

    if action == '1':
        print("---Encryption---")
        text = input("[+] Enter text: ")
        key = int(input("[+] Enter key (0-25): "))
        ciphertext = encrypt(text, key)
        print(f"[+] Cipher text: {ciphertext}")
    elif action == '2':
        print("---Decryption---")
        text = input("[+] Enter text: ")
        key = int(input("[+] Enter key (0-25): "))
        plaintext = decrypt(text, key)
        print(f"[+] Plain text: {plaintext}")
    else :
        print("Wrong Choice!")

if __name__ == '__main__':
    main()