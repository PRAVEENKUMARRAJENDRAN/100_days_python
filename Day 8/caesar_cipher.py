
def encode(char_postion , shift_number):
    return char_postion + shift_number



def decode(char_postion , shift_number):
    return char_postion - shift_number


def shift_function(encode_decode, shift_number, message):
    lowercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    cipher_text = ""
    for i in message.lower():
        if encode_decode == "encode":
            cipher_index = encode(lowercase_alphabets.index(i), shift_number)
            cipher_text += lowercase_alphabets[cipher_index]
        elif encode_decode == "decode":
            cipher_index = decode(lowercase_alphabets.index(i), shift_number)
            cipher_text += lowercase_alphabets[cipher_index]
        else:
            continue

    print(cipher_text)

shift_function("decode", 10, "rovvy")


        