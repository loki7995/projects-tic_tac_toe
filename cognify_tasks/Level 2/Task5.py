import string
import os
print("Current working directory:", os.getcwd())

def count_words_in_file(filename):
    word_count = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.translate(str.maketrans('', '', string.punctuation))
                words = line.lower().split()

                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1

        # Display results in alphabetical order
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print("Error: File not found.")


# Example usage
filename = input("Enter the filename: ")
count_words_in_file(filename)

#OUTPUT
'''
Current working directory: E:\python practice
Enter the filename: cognify_tasks\Level 2\programming_languages.txt
c: 2
css: 1
django: 1
html: 1
java: 1
python: 1
react: 1
sql: 1'''
