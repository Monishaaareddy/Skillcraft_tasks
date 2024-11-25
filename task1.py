alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alphabets[new_position]
        else:
            cipher_text += char
        print(cipher_text)
def decryption(cipher_text,shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position-shift_key)%26
            plain_text+=alphabets[new_position]
        else:
            plain_text += char
        print("after decryption")
        print(plain_text)
proceed_or_not=False
while not proceed_or_not:
    Go_to = input("Encrypt or Decrypt")
    text = input("type it in")
    shift = int(input("shift_key:"))
    if Go_to == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif Go_to == "decrypt":
        decryption(text, shift)
    play_again=input("enter 'yes' if u wanna continue else 'no'")
    if play_again=="no":
        proceed_or_not = True
        print("goodbye")

