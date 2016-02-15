import random
import string


def Xor(a_str, b_str):
  bits = ''

  if len(a_str) != len(b_str):
    return 'not equal length'
  else:
    for i in range(len(a_str)):
      if a_str[i] != b_str[i]:
        bits += '1'
      else:
        bits += '0'
  return bits


# {:08b} converts an integer to binary
# ord(c) Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string.
# so {:08b}.format(number) formats number into binary

def ToBin(input_str):
  str1 = ''
  for c in input_str:
    str1 += '{:08b}'.format(ord(c))
  return str1

def ToAsc(bin_text):
  str1 = ''
  for i in xrange(0, len(bin_text), 8):
    str1 += chr(int(bin_text[i:i+8], 2))
  return str1


message = raw_input('--> ')
print("Message: " + message)
message_bit_string = ToBin(message)

key = ''
for i in range(len(message)):
  key += random.choice(string.ascii_uppercase + string.digits)

print("Key:", key)
key_bit_string = ToBin(key)

encrypted_message = Xor(message_bit_string, key_bit_string)
print("encrypted message in binary = " + encrypted_message + '\n')
print("encrypted message in ASCII = " + ToAsc(encrypted_message) + '\n')

print("decrypt message with the password")
decrypted_message = Xor(encrypted_message, key_bit_string)
print("message decrypted = " + str(decrypted_message == message_bit_string))
print("message in binary is: " + '"' + str(decrypted_message) + '"\n\n')
print("message in Ascii is: " + '"' + ToAsc(str(decrypted_message)) + '"\n\n')
