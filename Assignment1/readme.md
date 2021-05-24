# Assignment 1

Write a program that takes some data as string input. Then it tries to find a positive number x such that when x is appended to the end of the string, the SHA256 hash of this new string is less than the target, which is

0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

Also print the time it takes to get this nonce value.

### input:
string input: athassin

### output:
The magic number is 918687

The time taken to get this nonce value is 3.1101319789886475 sec

## Explanation:
string+x is encoded into 'utf-8' and then passed to sha256 using hashlib to get hexadecimal output

int of the target is compared with int of this hexadecimal output and the first x which satisfies the condition is printed

time taken to execute this is found using time.time() and time.sleep()
