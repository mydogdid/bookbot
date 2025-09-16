from stats import count_words, count_characters
filepath = "books/frankenstein.txt"

#count_words(filepath)
        
total_characters = count_characters(filepath)
#print(total_characters)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {filepath}")

print("----------- Word Count ----------")
print(f"Found {count_words(filepath)} total words")

print("--------- Character Count -------")