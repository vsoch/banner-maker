# Prepare myconnectome logo data for graphic

import string
import random
import sys

""" hidden: string (with spaces between letters) to hide
rows: total number of rows
row: row for hidden text
length: row length
"""

def generate(hidden,rows=3,row=2,length=124,color="#CCC",color_hidden="#000"):

    hidden = list(hidden)

    # Generate a random set of letters
    abc = string.letters.upper()
    letters = []
    for rr in range(rows):
        letters.append([random.choice(abc) for r in range(length)])

    # Matched to colors
    colors = []
    for rr in range(rows):
        colors.append([color for r in range(length)])


    # Put in the hidden word
    for h in range(len(hidden)):
        letters[row-1][h+4] = hidden[h]
        colors[row-1][h+4] = color_hidden

    # Generate x and y coordinates
    xcoords = []
    ycoords = []
    letter_vector = []
    color_vector = []
    for l in range(len(letters)):
        for ll in range(len(letters[l])):
            xcoords.append((ll*30)+10)
            ycoords.append(l*20)
            letter_vector.append(letters[l][ll])
            color_vector.append(colors[l][ll])

    # Return letters, colors, xcoords, ycoords
    return letter_vector, color_vector, xcoords, ycoords
