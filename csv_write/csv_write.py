import json
import re
import itertools
import os
from collections import Counter

# global variable keeping track of seen genre_names
sorted_genre_names = []
genre_names = []
visualized_genre_names = [
    'hip hop',
    'rap',
    'pop',
    'trap',
    'funk',
]

### 
# Potential way of accounting for popularity of all genres by score
    # dict_genre_count = Counter(genre_names)
    # for genre in dict_genre_count.keys():
    #     if dict_genre_count[genre] == 1:
    #         sorted_genre_names.append(genre)
    #     else:
    #         break
###
def print_genre_names():
    fileInput = ""
    inputFile = open(fileInput)  # open json file
    data = json.load(inputFile)  # load json content
    inputFile.close()  # close the input file
    for song_name in data.keys():
        for genre in data[song_name]["genre"]:
            if genre not in genre_names:
                genre_names.append(genre)
            sorted_genre_names.append(genre)
    sorted_genre_names.sort()
    print(sorted_genre_names)


def find_most_freq_genre(genres):
    genre_string = "".join(genres)
    # what to do it most frequent genre is not in genre_names?
    seqs = re.findall(str.join('|', genre_names), genre_string)
    grps = [(key, len(list(j))) for key, j in itertools.groupby(seqs)]
    res = max(grps, key=lambda ele: ele[1])
    return res


def main():
    # gives us a visualization of genre names which we hand sort
    print_genre_names()
    # if you are not using utf-8 files, remove the next line
    # sys.setdefaultencoding("UTF-8") #set the encode to utf8
    # check if you pass the input file and output file
    fileInput = ""
    inputFile = open(fileInput)  # open json file
    data = json.load(inputFile)  # load json content
    inputFile.close()  # close the input file
    for song_name in data.keys():
        for genre in data[song_name]["genre"]:
            most_freq = find_most_freq_genre(genre)[0]
            file_name = "" + most_freq + ".csv"
            if not os.path.exists(file_name):
                append_write = "w"
            else:
                append_write = "a"
            with open(file_name, append_write) as f:
                url_name = data[song_name]["url"]
                f.write(url_name + "," + "\n")
            f.close()


if __name__ == '__main__':
    main()
