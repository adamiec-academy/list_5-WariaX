def words_from_file(file):
    words = []
    for x in open(file, encoding="utf-8"):
        words.append(x.strip())

    return words


def longest_word(): 
    words = words_from_file("words.txt")

    result_max = words[0]  
    for word in words: 
        if len(word) > len(result_max):
            result_max = word  

    return result_max
