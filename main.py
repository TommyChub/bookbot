import string

def main():
    book_path = "books/frankenstein.txt"
    report = generate_report(book_path)
    print(report)

def generate_report(path):
    book_text = get_book_text(path)
    word_count = get_word_count(book_text)
    dict_list = get_char_count(book_text)
    #sorted_dict = char_dict.sort()

    print(f'--- Begin report of {path} ---')
    print(f'{word_count} words found in the document')
    print('')
    for dict in dict_list:
        print(f"The '{dict['character']}' character was found {dict['count']} times")
    print(f'--- End report ---')

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def sort_on(dict):
    return dict['character']

def get_char_count(book_text):
    char_list = []
    for char in book_text:
        char_lower = char.lower()
        if char_lower.isalpha():
            if not any(row.get('character') == char_lower for row in char_list):
                char_list.append({'character': char_lower, 'count': 1})
            else:
                update_row = next((row for row in char_list if row['character'] == char_lower), None)
                update_row['count'] += 1

    char_list.sort(key=sort_on)
    return char_list
    
main()