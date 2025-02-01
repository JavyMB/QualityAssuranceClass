# pylint: disable=invalid-name
""" Program that count words in file """
import sys
import time

def count_words(data):
    """ Count words in a list of strings """
    word_count = {}
    for line in data:
        words = line.split()
        for word in words:
            word = word.strip().lower()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count

def count_words_in_file(file_path):
    """ Count words in a file and return the word count """
    word_count = {}

    try:
        with open(file_path, 'r',encoding="utf-8") as file:
            # Read each line from the file
            for line in file:
                # Split the line into words by spaces and handle invalid words
                words = line.split()
                for word in words:
                    word = word.strip().lower()
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return word_count

def write_results(word_count, elapsed_time):
    """ Write results to a file and display them on the screen """
    # Write results to a file and display it on the screen
    with open("WordCountResults.txt", "a",encoding="utf-8") as result_file:
        result_file.write("Row Labels\tCount of TC2\n")
        for word, count in word_count.items():
            result_file.write(f"{word}\t{count}\n")

        result_file.write(f"\nGrand Total\t{sum(word_count.values())}\n")
        result_file.write(f"\nTime Elapsed: {elapsed_time:.4f} seconds\n")

    # Display results on the screen
    print("Row Labels\tCount of TC2")
    for word, count in word_count.items():
        print(f"{word}\t{count}")

    print(f"\nGrand Total\t{sum(word_count.values())}")
    print(f"\nTime Elapsed: {elapsed_time:.4f} seconds")

def main():
    """ Main function """
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <fileWithData.txt>")
        sys.exit(1)

    file_name = sys.argv[1]
    # Start timer
    start_time = time.time()
    # Count words in the file
    word_count = count_words_in_file(file_name)
    # Stop timer
    elapsed_time = time.time() - start_time
    # Write and display results
    write_results(word_count, elapsed_time)

if __name__ == "__main__":
    main()
