#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = ''
    sent_len = len(sentence)
    if sentence == '':
        first_char = None
    else:
        first_char = sentence[0]
    return sent_len, first_char
