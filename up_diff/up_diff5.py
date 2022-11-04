#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word1 = input('enter first word: ')
    word2 = input('enter second word: ')
    k = 0
    for i in word1:
        print(k + 1, " letter ", i in word2)
        k += 1
