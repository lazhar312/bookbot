from string import ascii_lowercase


def get_book_text(filepath):
    # Get a filepath, returns a string 

    with open(filepath) as f:
        file_content = f.read()

    return file_content


def get_num_words(my_string):
    #Get a string, returns word count

    return len(my_string.split())


def get_num_letters(my_string):
    # Get a string, return a dict with all char count in lowercase

    char_count={}
    for char in my_string : 
        char = char.lower()

    # Catches KeyErrors and creates a key instead
        try:
            char_count[char] += 1  
        except KeyError as e : 
            char_count[char] = 1

    return char_count


def character_count_report(dico):
    
    sorted_list = sorted(dico.items(), key = lambda x:x[1], reverse=True)
    sorted_list_alphaonly = []

    for item in sorted_list: 
        if item[0].isalpha():
            sorted_list_alphaonly.append(item)

    sorted_dict = dict(sorted_list_alphaonly)   

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    for i in sorted_dict:
        print(f"{i}: {sorted_dict[i]}")
    
    return sorted_dict