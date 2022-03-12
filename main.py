# Python script to convert OpenLP exported files, which are in .XML format to .TXT format,
# which is accepted by ProPresenter while importing.
# This code only considers the lyrics in the first verse, i.e. (V1) in OpenLP song editor.!\
# Will convert all the lyrics in V1 to text files, if you are confused go through OpenLP song editor.

import xml.etree.ElementTree as ET
import os


# Have to make changes here to consider other verses/ chorus,etc. Experiment with root[1] at line 16;
# By changing the values in [], and the following for loops.

def getLyrics(directory_name, file):
    f = os.path.join(directory_name, file)
    tree = ET.parse(f)
    root = tree.getroot()
    song_lyrics = ''
    for txt in root[1]:
        song_lyrics += root[1][0][0].text

        for c in txt.iter():
            if c.tail != None:
                song_lyrics += str(c.tail)
                song_lyrics += '\n'
    song_lyrics = os.linesep.join([s for s in song_lyrics.splitlines() if s])
    return song_lyrics

def createTextfile(song_lyrics, file, out_directory):
    txtfile = str(file)                                                     # Converting filename to string
    txtfile = txtfile[0:-4] + '.txt'                                        # Replacing .xml to .txt
    g = open(out_directory+txtfile, "w+", encoding='utf8')              # encoding='utf8' is mandatory for languages other than English
    g.write(song_lyrics)
    g.close()


if __name__ == "__main__":
    xml_directory = 'input_path'                                                  # Path of where the XML files are located.
    output_directory = 'output_path'                                                # Path of where the text files will be saved to.

    for filename in os.listdir(xml_directory):
        lyrics = getLyrics(xml_directory, filename)
        createTextfile(lyrics, filename, output_directory)
