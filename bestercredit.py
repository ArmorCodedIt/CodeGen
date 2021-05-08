import string
import random
import requests
import os,sys
import subprocess
import glob
from os import path


f = open('credit.txt','w')
sys.stdout = f

letters = string.digits

print(''.join(random.choice(letters) for i in range(15)))

letters = string.digits

print(''.join(random.choice(letters) for i in range(3)))

letters = string.digits

print(''.join(random.choice(letters) for i in range(4)))

letters = string.digits

print(''.join(random.choice(letters) for i in range(2)))
