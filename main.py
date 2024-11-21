def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    num_words = get_num_words(text)
    num_char = num_of_char(text)
    
    
    
    print(f"{num_words} words found in the document")
    
def get_num_words(text):
    words = text.split()
    return len(words)
        

def get_book_path(path):
    with open(path) as f:
        return f.read()
    
def num_of_char(text):
    dictionary = {}
    for char in text:
        if char.isalpha():
            lowered_char = char.lower()
            if lowered_char in dictionary:
                dictionary[lowered_char] += 1
            else:
                dictionary[lowered_char] = 1
                
            
    return dictionary
    
def sort_on(dict):
    return dict["num"]


def process_chars(dictionary):
    
    char_list = []
    for char, count in dictionary.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
        
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()