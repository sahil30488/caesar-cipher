alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt and q for quit:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
  cipher = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    new_letter = alphabet[new_position]
    cipher += new_letter
  print(f"The encoded text is {cipher}")


def decrypt(text,shift):
  decipher=''
  for words in text:
    pos=alphabet.index(words)
    new_pos=pos-shift
    new_words=alphabet[new_pos]
    decipher+=new_words
  print(f'the decipher word is  {decipher}')

if direction == 'encode' :
  
  encrypt(text,shift)
elif direction == 'decode':
  decrypt(text, shift)
else :
  exit()