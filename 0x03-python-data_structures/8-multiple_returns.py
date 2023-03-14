#!/usr/bin/python3
def multiple_returns(sentence):
<<<<<<< HEAD
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
=======
    s = len(sentence)
    a = (s, sentence[0])
    return a
>>>>>>> 8b0b14f75ac72c18d737d93b69dcb40c633b532e
