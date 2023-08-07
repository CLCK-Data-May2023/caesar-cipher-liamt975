def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            start = ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plain_text = input("Please enter a sentence: ")
    shift = 5
    encrypted_text = caesar_cipher_encrypt(plain_text.lower(), shift)
    print("The encrypted sentence is:", encrypted_text)

if __name__ == "__main__":
    main()
# add your code here

