Setup:
After downloading the zip file containg python and html code, you will need to install the pycryptodome library. This is done by running "pip install pycryptodome" in the terminal. If this doesn't work, try using "sudo pip install pycryptodome" to make sure you have full permissions. Then, you can access the website by first moving into the directory "rsa-final-project" by typing "cd rsa-final-project" into the command line. Then use "flask run" and click on the link, and the website will open.

Usage:
This website has three functions, key generation, encryption, and decryption. If you want to have a message sent to you, refer to the key generation and decryption sections. If you want to send a message, refer to the encryption section.

Key Generation:
This feature allows you to generate a key for RSA. This does not require any user input, as the size of the keys are preset to a reasonable length. Simply click on the button to generate a key consisting of a d value, an e value, and an n value. Then copy the three numbers and save them wherever you wish. The e and n values are public - send them to the person you want to send a message to you. You can then use your d value and the n value in the decryption section to decrypt it.

Encryption:
In order to encrypt a message, you must have recieved an e and n value from the person you want to send the message to. You input these values, along with your message, on this page, then you will recieve a number that is your encrypted message. Send that number to the recipient, who can then decrypt it using this website.

Decryption:
Use this page after generating a key for yourself and recieving an encrypted message. Then, input the d and n values that you have saved, as well as the message you recieved. Then you will have your decrypted message!

Video Demonstration:
https://youtu.be/Ux3i2Y3NPNI
