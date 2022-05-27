# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as file_content:
        content = file_content.read()
        
    return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    
    list_of_words = text.split(' ')
    count_of_words = {}
    
    # Looping throught the list of words and the adding each word as key and the number of its occurences as value into the empty dictionary
    for word in list_of_words:     
        if word in count_of_words:
            count_of_words[word] += 1
        else:
            count_of_words[word] = 1
    return count_of_words
