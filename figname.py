os .system ("pip install pyfiglet")
import os


import pyfiglet

Z = '\033[1;31m' #احمر

X = '\033[1;33m' #اصفر

Z1 = '\033[2;31m' #احمر ثاني

F = '\033[2;32m' #اخضر

A = '\033[2;34m'#ازرق

C = '\033[2;35m' #وردي

B = '\033[2;36m'#سمائي

Y = '\033[1;34m' #ازرق فاتح

M = '\x1b[1;37m'#ابیض

name = input (X+"Enter your name ----> ")

print (B+"""

1-Red

2-yellow

3-green

4-blue

5-light blue

""")

color = input ("What color you need? --->")

py = pyfiglet.figlet_format(name)

os .system ("clear")

print ("Welcome " + name)

if color =="1":

	print (Z+py)	

	

elif color =="2":

	print (X+py)

	

	

elif color =="3":

	print (F+py)

	

	

elif color =="4":

	print (A+py)

	

	

elif color =="5":

	print (B+py)

else:

	print ("error")




