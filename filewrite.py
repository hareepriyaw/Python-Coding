# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:53:09 2022

@author: jahna
"""
import math
ads=open("try.txt", "w")
yam=["I am a woman", "I am a teacher", "I am a wife", "I am a writer", "I am a devotee", "I am a programmer"]
ads.writelines(yam)
ads.close()
ads=open("try.txt", "r")
print("this is written to the file", ads.read())
