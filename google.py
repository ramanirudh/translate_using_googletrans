
## Program to translate using google translate
## Do not continuously translate. Give a break of atleast 30 minutes after every job
## Uses googletrans package available in python
## Ram Anirudh ## 30 Dec 2019 ## 5 Mar 2024
## Filenames are hard-coded. To translate a file, search "Input" comment line and type filename in the "open" function call. Do the same for "Output". Save the program and run in python
## I ran the program using python2

import io
from googletrans import Translator

translator = Translator()

## Input
file = io.open('xad','r')

## Output
outfile = io.open('xad_google.hi','w',encoding='utf-8')

for each in file:
    trans = translator.translate(each,dest ='hi')
    #print(trans.text)
    outfile.write(trans.text)
    outfile.write(u'\n')
    
outfile.close()
file.close()

