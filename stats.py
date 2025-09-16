def get_book_text(filepath):
    with open(filepath) as f:
        read_book = f.read()
    return read_book
def main(bookpath):
    print(get_book_text(bookpath))


def count_words(bookpath):
    words = get_book_text(bookpath).split()
    num_words = 0
    for word in words:
        num_words += 1
    #print(f"{num_words} words found in the document")
    return num_words

def count_characters(bookpath):
    characters = get_book_text(bookpath).lower()
    total_count = {}
    count = 0
    for character in characters:
       if character not in total_count:
           total_count[character] = count
       if character in total_count:
           total_count[character] += 1
    return total_count

def sort_on(items):
    return items["num"]

def report(bookpath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")

    print("----------- Word Count ----------")
    print(f"Found {count_words(bookpath)} total words")

    print("--------- Character Count -------")
