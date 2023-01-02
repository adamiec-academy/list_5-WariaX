def words_from_file(file):
    data = []
    for x in open(file, encoding="utf-8"):
        data.append(x.strip().split(4 * " "))
        
    return data


def longest_word(words): 
    result_max = words[0]  
    for word in words: 
        if len(word) > len(result_max):
            result_max = word  

    
    
    return result_max


words = words_from_file("words.txt")


print(longest_word(words))
