# RSA
An encryption for messages
Uses two dictionaries to convert letters into numbers, and numbers into letters
public and private keys are created in line 53
The funtion keys will give you the public and private keys.
when creating keys the numbers given to the keys funtion need to be prime
To encrypt any message use the funtion encrypt by giving it the two public keys and the message
Example: encrypt(public, public2, "your message goes here")
To decrypt the encrypted message use the funtion decrypt by giving it the two private keys and the array of encrypted letters
Example: print(decrypt(private, private2, encrypt(public, public2, "your message goes here")))
