#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_a = ()
    b = len(sentence)
    if b <= 0:
        first = None
        tuple_a = (b, first)
    else:
        tuple_a = (b, sentence[0])

    return tuple_a
