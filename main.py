def print_report(character_count_list, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for item in character_count_list:
        print(f"The '{item[1]}' character was found {item[0]} times")
    print("--- End report ---")
    
    
def get_letter_count(file_contents) -> dict:
    c_dict = {}
    for c in file_contents:
        if c.isalpha():
            if c.lower() not in c_dict:
                c_dict[c.lower()] = 1
            else:
                c_dict[c.lower()] += 1
    return c_dict
    

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    
words = file_contents.split()

c_dict = get_letter_count(file_contents)
   
c_list = []
for k in c_dict:
    c_list.append([c_dict[k], k])
    
c_list.sort(reverse=True)

print_report(c_list, len(words))




