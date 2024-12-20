def main():
    file_location = "books/frankenstein.txt"
    text = file_text(file_location)
    words_total = word_count(text)
    characters_total = character_count(text)
    characters_list = dictionary_to_list(characters_total)
    characters_list.sort(reverse=True, key=lambda x: x["count"])
    #report formatting section
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_total} words found in the document")
    print()
    for char_dict in characters_list[:]:
        print(f"The '{char_dict['character']}' character was found {char_dict['count']} times")
    print("--- End report ---")

def word_count(text):
#counts the number of words in the opened file
    words = text.split()
    return len(words)

def character_count(text):
#counts the number of times each character appears in the opened file
    lowered_string = text.lower()
    character_dictionary ={}
    for x in lowered_string:
        character_dictionary[x] = character_dictionary.get(x, 0) + 1
    return character_dictionary

def dictionary_to_list(characters_total):
#take the dictionary and returns the value of the letter key as a list
    character_list =[]
    for character, count in characters_total.items():
        if character.isalpha():
            character_list.append({"character": character, "count": count})
    return character_list

def file_text(path):
#opens the file and reads the contents as a string
    with open(path) as f:
        return f.read()

main()