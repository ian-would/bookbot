def main():
    file_location = "books/frankenstein.txt"
    text = file_text(file_location)
    words_total = word_count(text)
    print(f"{words_total} words found in the document")

def word_count(text):
#counts the number of words in the opened file
    words = text.split()
    return len(words)

def character_count(text):
#counts the number of times each character appears in the opened file


def file_text(path):
#opens the file and reads the contents as a string
    with open(path) as f:
        return f.read()

main()