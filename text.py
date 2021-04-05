# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 19:40:28 2021

@author: Eliezer
"""

def revword(word:str):
    return word.lower()[::-1]



def countword():
    f = open("text.txt", "r")
    words = f.read().replace("\n", " ").split(" ")
    f.close()
    
    key_word = words[0].lower()
    counter = 1
    
    for word in words[1:]:
        if revword(word) == key_word:
            counter += 1
    
    
    return counter
