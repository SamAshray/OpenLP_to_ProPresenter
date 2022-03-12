# Messier looking version of main.py, but both are same in function and output.
import xml.etree.ElementTree as ET
import os

# Iterating over the files in directory with xml files.
directory = 'C:/...'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    tree = ET.parse(f)
    root = tree.getroot()
    lyrics = ''
    for txt in root[1]:
        lyrics += root[1][0][0].text

        for c in txt.iter():
            if c.tail != None:
                lyrics += str(c.tail)
                lyrics+= '\n'
    lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])         # Gotten all the lyrics in string format.


    
    # Saving as text file, with same name as the xml file.

    file = str(filename)
    file.replace('(Telugu)', ' ')                                           # Replacing (Telugu) which is the author name, in filename
    file = file[0:-4] + '.txt'
    print(file)
    g = open("C:/...", encoding='utf8')                              # Mandatory step for languages other than English, esp. Telugu
    g.write(lyrics)
    g.close()

