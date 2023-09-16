# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 17:38:56 2023

@author: 69ami
"""

def most_frequent(input_string):
    
    input_string = input_string.replace(" ", "").lower()
    
    letter_count = {}
    
    
    for letter in input_string:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
                
                
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

    for letter, frequency in sorted_letters:
        print(f"{letter}: {frequency}")
        
input_str = 'messi is the goat'
most_frequent(input_str)
