#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word1 = input('enter first word: ')
    word2 = input('enter second word: ')
    k = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            k += 1
    print(k)
