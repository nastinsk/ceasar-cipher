# Ceasar cipher implementation

**Author**: Anastasia Lebedeva

## Challenge
Devise a function to encrypt a message that can then be decrypted when supplied with the corresponding key.
Write a function to decrypt text than was encrypted with ceasar cipher without a key


## Architecture
* Python 3.7.5
* Pipenv
* Pytest
* nltk words collection
* collections.Counter


## API
1. encrypt_(plain, key) - Function that takes in a plain text phrase and a numeric key and encrypts it useng ceasar cipher with the shift equals to key. The plain text can be anything in english letters, function will return encrypted lowercased text with the original punctuation marks and spaces
2. decrypt_(cipher, key) - Function that takes in encrypted text and numeric key which will restore the encrypted text back to its original form as long as correct key is supplied
3. break_cipher(cipher) - Function to transform cipher into its original state without access to the key.
4. is_english(text) - Helper function to find out if the given text is english text or not



## Materials used
* Fragment from "The Hobbit" by J. R. R. Tolkien	
* [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
