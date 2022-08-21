""" This program will encrypt and decrypt the input message"""
from os import system

def crypt(msg):
    keys=" abcdefghijklmnopqrstuvwxyz0123456789+-*/.,@\!#$%^&`~()|[]"
    values=" !@0#.2/*1|[,3)]$&^%\(abc+d9efopq8rsjkl6mtu7g~hi-`n5vwx4yz"
    
    encrypt=dict(zip(keys,values))
    decrypt=dict(zip(values,keys))
    
    mode=input("\nEnter mode : ('E' : Encryption and  'D' : Decryption) :- ").upper()

    cryptMsg=""
    if mode=='E':
        cryptMsg="".join(encrypt[char] for char in msg).upper()
    elif mode=='D':
        cryptMsg="".join(decrypt[char] for char in msg).upper()
    else:
        print("\n\t....Enter correct choice...\n")

    print("\n",'*'*40)

    return cryptMsg

print("\t...Empty message will terminate the program....")
msg=" "
while msg!="":
    msg=input("\nEnter message : ").lower()
    if msg=="":
        exit()
    print("\n",crypt(msg),"\n")
