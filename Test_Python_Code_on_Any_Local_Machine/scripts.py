# Name: Anay Abhijit Joshi
# CS 5165/6065:  Introduction to Cloud Computing
# Date: October 9, 2024
# Project 3: Docker

# Here are the necessary libraries and modules.
import re
from collections import Counter
import socket
import os

# File paths
# Using a '.' at the beginning of each file path to indicate the current directory
file1_path = "./home/data/IF.txt"
file2_path = "./home/data/AlwaysRememberUsThisWay.txt"
output_path = "./home/data/output/result.txt"

# Test file path to see if contactions are handled correctly in 'AlwaysRememberUsThisWay.txt'
test_file_after_contractions = "./home/data/output_handled_contractions_file_2/AlwaysRememberUsThisWay_AfterContraction.txt"

# Read the file(s)
def read_file(filepath):
    # Read the file and return its contents
    with open(filepath, 'r') as file:
        # Return the contents of the file in uppercase to make it case-insensitive
        return file.read().upper()

# Clean text by removing punctuation and extra spaces
def clean_text(text):
    # Remove punctuation and extra spaces from the text
    text = re.sub(r'[^\w\s]', '', text)
    # Return the cleaned text
    return text

# Count the number of words in the text
def count_words(text):
    # Split the text into words and return the number of words
    words = text.split()
    # Return the number of words
    return len(words)

# Count the frequency of words in the text
def word_frequencies(text):
    # Use the clean_text function to clean the text
    text = clean_text(text)
    # Split the text into words and count the frequency of each word
    words = text.upper().split()
    # Return the frequency of words
    return Counter(words)

# Handle contractions in the text by expanding them
def split_contractions(text):
    # Define a dictionary of the contractions in 'AlwaysRememberUsThisWay.txt' and their respective expansions
    contractions = {
        "IT'S": "It is",
        "COULDN'T": "could not",
        "I'M": "I am",
        "CAN'T": "can not",
        "WON'T": "will not",
        "I'LL": "I will",
        "DON'T": "do not",
        "YOU'RE": "You are",
        "THAT'S": "that is"
    }
    # Replace the contractions with their expansions in the text
    for contraction, expansion in contractions.items():
        # Replace the contraction with its expansion in the text
        text = text.replace(contraction, expansion)
        # Return the text with contractions expanded
    return text

# Determine the IP address of the machine running the container.
def get_ip_address():
    # Get the hostname and IP address of the machine
    hostname = socket.gethostname()
    # Get the IP address of the machine
    ip_address = socket.gethostbyname(hostname)
    # Return the IP address of the machine
    return ip_address


# Main function
def main():
    # Read the contents of the files
    if_text = read_file(file1_path)
    always_remember_text = read_file(file2_path)

    # Count the number of words in both the files
    if_text_word_count = count_words(if_text)
    always_remember_text_word_count = count_words(always_remember_text)

    # Handle contractions in the text for file - 'AlwaysRememberUsThisWay.txt'
    always_remember_text_with_contractions = split_contractions(always_remember_text)
    # Count the number of words in the text after handling contractions
    always_remember_text_word_count_with_contractions = count_words(always_remember_text_with_contractions)

    # Write the text with contractions handled to a test file to check if everything is handled correctly
    with open(test_file_after_contractions, 'w') as new_file:
        new_file.write(always_remember_text_with_contractions)

    # Calculate the grand total number of words in both files (before and after handling contractions)
    grand_total_words = if_text_word_count + always_remember_text_word_count
    grand_total_words_with_contractions = if_text_word_count + always_remember_text_word_count_with_contractions

    # Top 3 most frequent words in 'IF.txt' and their respective counts
    if_word_freq = word_frequencies(if_text).most_common(3)

    # Top 3 most frequent words in 'AlwaysRememberUsThisWay.txt' after handling contractions and their respective counts
    always_remember_word_freq = word_frequencies(always_remember_text_with_contractions).most_common(3)

    # Get the IP address of the machine running the container
    ip_address = get_ip_address()

    # Finally, write the results to the output file - 'result.txt'
    with open(output_path, 'w') as output_file:
        # My Name
        output_file.write(f"Name: 'Anay Abhijit Joshi'\n\n")
        # All the required information
        output_file.write(f"Total Words Count in IF.txt: {if_text_word_count}\n")
        output_file.write(f"Total Words Count in AlwaysRememberUsThisWay.txt (before handling contractions): {always_remember_text_word_count}\n")
        output_file.write(f"Grand Total Words Count in both files (before handling contractions in 'AlwaysRememberUsThisWay.txt'): {grand_total_words}\n\n")
        output_file.write(f"Total Words Count in IF.txt: {if_text_word_count}\n")
        output_file.write(f"Total Words Count in AlwaysRememberUsThisWay.txt (after handling contractions): {always_remember_text_word_count_with_contractions}\n")
        output_file.write(f"Grand Total Words Count in both files (after handling contractions in 'AlwaysRememberUsThisWay.txt'): {grand_total_words_with_contractions}\n\n")
        # Top 3 most frequent words in both files, cases not considered: 
        #   1. Words which require handling of contractions like 'you'll' and 'you've', so 'you' is not counted as a separate word and won't be considered in word count of YOU
        #   2. Cases with '-and' and 'and-', so 'and' is not counted as a separate word and won't be considered in word count of 'AND'. 
        output_file.write(f"Top 3 Most Frequent Words and their Respective Counts in IF.txt ('not-considered words which require handling of contractions like you'll/you've' and 'cases with -and/and-'): {if_word_freq}\n\n")
        output_file.write(f"Top 3 Most Frequent Words and their Respective Counts in AlwaysRememberUsThisWay.txt (after handling contractions): {always_remember_word_freq}\n\n")
        output_file.write(f"IP Address of the Machine running the Container: {ip_address}\n")

    # Print the contents of the output file ('result.txt') to the console before exiting
    with open(output_path, 'r') as result_file:
        # Print the contents of the output file ('result.txt') to the console
        print(result_file.read())

# Run the main function if the script is executed
if __name__ == "__main__":
    # Create the output directory if it does not exist to save the output file ('result.txt')
    os.makedirs("./home/data/output", exist_ok=True)
    # Run the main function
    main()