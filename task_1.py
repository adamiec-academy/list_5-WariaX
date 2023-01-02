def words_from_file(file):
    words = []
    for x in open(file, encoding="utf-8"):
        words.append(x.strip())

    return words
    
words = words_from_file("words.txt")

def longest_word(words): 
    result_max = words[0]  
    for word in words: 
        if len(word) > len(result_max):
            result_max = word  

    
    
    return result_max
