#!/usr/bin/env python3


import os
import click
import secrets
from sys import exit
from output import message as m


KEY = ''
KEYLENGTH = 0


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
@click.option('--mode','-m',help="Decode a message",type=click.Choice(['encode','decode']),required=True)
@click.option('--text','-t',help="Put a string in directly (for small messages)",type=click.STRING)
@click.option('--input','-i',help="File containing message to encode/decode",type=click.STRING)
@click.option('--output','-o',help="File to write output to",type=click.STRING)
@click.option('--key','-k',help="Secret key from kfsecret.py",type=click.STRING,required=True)
@click.option('--show','-s',help="Print encoded message to stdout",is_flag=True)

def main(mode, text, input, output, show, key):

    global KEY
    global KEYLENGTH

    m('Now opening the key file. This will take a moment for large keys...',status='attention')
    with open(key, 'r') as f:
        KEY = f.read()

    KEYLENGTH = len(KEY)
    m(f"Key of length {KEYLENGTH} loaded")

    if text and input:
        m("The text flag and input flag cannot be used together.")
        exit(1)

    if input:
        with open(input, 'r') as f:
            text = f.read()

    if mode == 'encode':
        processed_message = encode_message(text)

    if mode == 'decode':
        processed_message = decode_message(text)

    if show:
        m(processed_message)
    
    if output:
        if os.path.exists(output):
            m('That file already exists!', status='error')
            exit(1)
        with open(output, 'w') as f:
            f.write(processed_message)


if __name__ == '__main__':
    main()
