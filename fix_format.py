#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:51:10 2017

@author: maxhully
"""

import os
import sys
import re

p = re.compile("<([^\.]+)>")

def exclude_line(line):
    return "<filename>" in line or "<foldername>" in line or line.strip() == ""

def process_text(text):
    match = p.search(text)
    if match:
        text = text.replace(match.group(0), match.group(1) + ":")
    return text.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c","\"").replace(u"\u201d", "\"").replace("\t","\n").replace(u"\u2026","...") + "\n"

def main(args):
    battery = []
    for name in os.listdir(args[0]):
        if name[-4:] == ".txt":
            battery.append(name)
    for source in battery:
        output = ""
        f = open(args[0] + "/" + source, encoding='utf-8')
        for line in f:
            if not exclude_line(line):
                output += process_text(line)
        target = "./Vanderbilt University/Altered/" + source
        f.close()
        g = open(target, 'w+', encoding='utf-8')
        g.write(output)
        g.close()


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        args = ['./Vanderbilt University']
    main(args)
