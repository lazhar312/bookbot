import stats
import sys
from stats import get_num_words
from stats import get_book_text
from stats import get_num_letters
from stats import character_count_report

def main():

    if len(sys.argv) != 2 :     # check number of provided arguments on call
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)             
    
    book_path = sys.argv[1]
    num_words = 0
    num_letters = {}

    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_letters = get_num_letters(book_text)



    # print(f"{num_words} words found in the document")
    print(num_letters)
    character_count_report(num_letters)


main()



