import hashlib
import itertools

print('Enter the MD5 hash:\n')

__decode__ = input()

def decrypt_md5(__decode__):
    chars = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+=-`,.<>/?;:'"
    for i in range(1, 21):
        for word in itertools.product(chars, repeat=i):
            test_word = ''.join(word)
            if hashlib.md5(test_word.encode()).hexdigest() == __decode__:
                return test_word
    return None

#__decode__ = "d41d8cd98f00b204e9800998ecf8427e" 

decrypted_word = decrypt_md5(__decode__)
if decrypted_word:
    print("The decrypted word is:", decrypted_word)
else:
    print("The hash could not be decoded.")
