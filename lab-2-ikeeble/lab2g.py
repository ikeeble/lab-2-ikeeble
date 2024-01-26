#!/usr/bin/env python3

#Author: Iain Keeble
#Author ID: ikeeble
#Date Created: 2024/01/26

import sys

if len(sys.argv) > 1:
    timer= int(sys.argv[1])
else:
    timer = 3
while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')    