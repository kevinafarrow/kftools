#!/usr/bin/env python3


import os
import click
import secrets
import pyperclip
from sys import exit
from output import message as m


KEY = ''
KEYLENGTH = 0
key = None
mode = None
show = None
file_out = None
clipboard = None


def encode_character(character):
    echaracter = ''
    while echaracter != character:
        position = secrets.randbelow(KEYLENGTH)
        echaracter = KEY[position]
    return position


def encode_message(message):
    emessage = []
    for c in message:
        emessage.append(encode_character(c))
    emessage = ','.join([str(e) for e in emessage])
    return emessage

def decode_message(message):
    return ''.join([ KEY[int(c)] for c in message.split(',') ])


@click.command()
@click.option('--key','-k',help="Secret key from kfsecret.py",type=click.STRING)
@click.option('--mode','-m',help="Decode a message",type=click.Choice(['encode','decode']))
@click.option('--file_in','-i',help="File containing message to encode/decode",type=click.STRING)
@click.option('--file_out','-o',help="File to write output to",type=click.STRING)
@click.option('--show','-s',help="Print encoded message to stdout",is_flag=True)
@click.option('--clipboard','-c',help="Copy text to clipboard.",is_flag=True)

def main(mode, file_in, file_out, show, key, clipboard):

    global KEY
    global KEYLENGTH

    if key == None:
        key = ''
        key = input('Please enter the location of the key: ')

    m('Now opening the key file. This will take a moment for large keys...')
    with open(key, 'r') as f:
        KEY = f.read()

    KEYLENGTH = len(KEY)
    m(f"Key of length {KEYLENGTH} loaded")

    if file_in:
        with open(file_in, 'r') as f:
            text = f.read()
    else:
        m('Entering interactive mode')
        m('Type /stop on its own line to signal completion.')
        text = ''
        while True:
            line = input('[-]  > ')
            if line == '/stop':
                break
            text += line

    if mode == None:
        show = None # This forces show back into interactive mode. 
        clipboard = None # Ditto
        mode = ''
        valid = ['encode', 'decode']
        while mode not in valid:
            mode = input('[!]  Please enter a valid mode (encode or decode): ').lower()

    if mode == 'encode':
        processed_message = encode_message(text)

    if mode == 'decode':
        processed_message = decode_message(text)

    if show == None:
        answer = ''
        valid = {'y': True, 'n': False}
        while answer not in valid.keys():
            answer = input('[!]  Do you want to show results in stdout? (yes or no): ').lower()[0]
        show = valid[answer]

    if show:
        m(processed_message)

    if clipboard == None:
        answer = ''
        valid = {'y': True, 'n': False}
        while answer not in valid.keys():
            answer = input('[!]  Do you want to copy the results to the clipboard? (yes or no): ').lower()[0]
        clipboard = valid[answer]

    if clipboard:
        pyperclip.copy(processed_message)

    if file_out == None:
        answer = ''
        valid = {'y': True, 'n': False}
        while answer not in valid:
            answer = input('[!]  Do you want to save this to a file? (yes or no): ').lower()[0]
        file_out = valid[answer]
        if file_out:
            file_out = input('[!]  Where would you like to put it?: ')
    
    if file_out:
        if os.path.exists(file_out):
            m('That file already exists!', status='error')
            exit(1)
        with open(file_out, 'w') as f:
            f.write(processed_message)


if __name__ == '__main__':
    main()
