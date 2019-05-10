#!/usr/bin/python3

import implementation as imp
import constants as c

#assigning configuration
print('Choose configuration #, where:\n\
0 - HEAT->iron->copper; 1 - HEAT->copper->iron')

configNumber = int(input('Your configuration is: '))
layers = [imp.layer0, imp.layer1]
if configNumber:
    layers = [imp.layer1, imp.layer0]
imp.layers = layers


# layer thicknesses
s0 = input('Input wall thicknesses in range 5..500mm\nEnter s0, mm: ')

s1 = input('Enter s1, mm: ')

s = [0.001*float(s0), 0.001*float(s1)]
c.s = s


TIME = float(input('Enter time of exposure in sec.: '))
c.TIME = TIME

print('Please wait, program is in process...')

import output
