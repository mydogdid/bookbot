from stats import count_words, sorted_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}")

print("----------- Word Count ----------")
print(f"Found {count_words(path)} total words")

print("--------- Character Count -------")
chars = sorted_dict(path)
for char in chars:
    ch = char["char"]
    if ch.isalpha():
        print(f"{ch}: {char["num"]}")