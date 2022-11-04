#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentence = input("enter your sentence, that will be altered: ")
    sentence = sentence.replace('c', '')  # for eng
    sentence = sentence.replace('с', '')  # for rus
    print(sentence)
