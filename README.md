# Toy DES server

This is a toy end to end Feistel cipher encrypted file sending service implemented for HW 1 of cryptography and network security 1 during the Fall 2018 semester. This server is written in python 2.7.

#### Details

This program reads in a file as a binary array of bytes, encrypts it using a 2 stage Feistel cipher, sends it to another computer over TCP, decrypts it, and saves the file locally on the remote machine. This program has two parts: the sending and receiving part. The sending server sends files over TCP in 1024 byte streams to the remote receiving machine at a time, and will continue while the remote machine returns with a "200 OK" signal. If the signal is not received within a timeout of 2 seconds or the connection is lost, both instances of the program will terminate. The remote server assumes the first message sent is the name of the file, and following messages will be the contents of the file. The remote server will stop listening after a message has been sent that is less than 1024 bytes long and write the decrypted contents of the file to memory.

#### Usage

To send a file to a certain IP address over a port:

```bash
python DES.py send filename IP port
```

NOTE: the listening port must already be initialized, listening, and ready for a file to be received before send can start properly. If this is not the case, the program will terminate and with an error that the connection was refused.

To listen and wait for files from a port:

```bash
python DES.py listen port
```

#### Implementation Details

The Feistel cipher is a multistage DES cryptosystem which manipulates the plaintext through multiple passes through an F function. The F function permutes and performs an XOR operation with the right hand side of the plaintext. This is followed by an extra XOR operation with the output of that F function and the left hand side of the plaintext. The left and right hand sides are then swapped and the process is repeated multiple times. For the purposes of this assignment, this cipher only performs 2 loops. However, by changing the `passes` variable in the code, one can alter the amount of passes the server performs to encrypt or decrypt the object. NOTE: both the sender and receiver should have the same number of passes, otherwise the the program will write a gibberish file to the remote computer. Furthermore, the 10 bit initial key is integral to both the secrecy of the file transfer as well as the consistent correct decryption of the file. It is also important that this value is exactly the same in both copies of the program. Keep in mind that in an actual software it would be extremely unsafe to have the key hard-coded in plaintext in the implementation, but for the purposes of this exercise, the key will be visible in the code. All functions are implemented such that they all represent an actual operation inside of the Feistel cipher flow chart. Files are sent consistently and correctly, however there is much room for improvement in terms the speed of sending and receiving files. For instance, a `284 kb` file took approximately 1 minute to send to the same machine, while downloading that same file from the internet would take less than one second.
