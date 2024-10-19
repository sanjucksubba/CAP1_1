# Dzongkha Spell Checker

## Project Overview
1. The propose of the project is it identifies and reports any words not found in the dictionary.
2. The main feature of the project is it validates a text file by checking each word against a dictionary, reporting unrecognized words with their line and 
   posituion, and supporting customizable input files for fixiable use.

# Table of content
- [Usage](#usage)
- [Implementation Details](#implementation_details)
- [Data Structures](#data-structures)
- [Algorithms](#aligorithms)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Improvements](#Future-improvements)
- [References](#references)

## Usage
Read Files: Load the words from dictionary.txt and 357.txt.
Check Words: For each word in 357.txt, check the word against the dictionary.
Report Errors: Print the word that is not in dictionary along with the line and position.

## Implementation Details
Dictionary: Loads the words from dictionary.txt.
Read File: Loads text from 357.txt.
Check Words: Check each word in the text against dictionary.
Report Errors: Print misspelled words with line and position.

## Data Structures
Dictionary File:
Purpose: A look-up list of valid words
Structure: A text file, plain - dictionary.txt - one word per line; against which each word in the text is checked.

Text File: 357.txt
Purpose: The text to be spell-checked
Structure: Multi-line text in which every word gets checked against the dictionary.

Reading Files:
Purpose: It reads and processes content from both files.
Structure: The 'with open' acts to safely read the files into lists to ensure proper resource management.

Spell Check Words:
Purpose: The program compares each word in the text file with the dictionary.
Structure: It splits every line into words and iterates over it for checking if there is a word in the dictionary.

Error Reporting:
Purpose: To find out and report the misspelled words.
Structure: Prints the misspelled word, its line number, and position.

## Alogorithms
Efficient Dictionary Lookup
Set Lookups: O(1) average time complexity.

Cleaning Dictionary File
List Comprehension w/ String Strip: All formatting made consistent - spaces, new lines, etc.

Reading Text and Lines
Enumerate: Line and word position kept efficiently.

Word Checking
Membership Testing: Each word tested for membership against dictionary.

## Performance Analysis
Time Complexity:
Reading the Files: O(n) where n is the number of lines in the files.
Set Lookup for Dictionary: In the average case, each word check has an O(1) time complexity.
Checking Words: O(m * k) where m is the number of lines in the text file and k is the average number of words per line.
Overall: The main operation done is checking each word; this makes it O(n + m * k), but since normally n and m * k are in comparable magnitudes, it simplifies to O(n).

Space Complexity:
Dictionary: O(d) where d = number of words in the dictionary.
Text to Check: O(t) where t = number of lines in the text file.
Overall: O(d + t), since both dictionary and text need to be stored.

Performance Optimizations:
Used Set for Dictionary: This uses a set instead of a list because sets allows O(1) lookups.
List Comprehension: The most efficient way to read and process the lines all at once
Memory Management:Using with open ensures files are closed automatically, saving memory.

## Challenges and Solutions
Unicode Handling:
Problem: To handle special characters while reading.
Solution: Used utf-8 encoding.

Efficient Dictionary Storage:
Problem: Speed up the lookups.
Solution: A set was used for O(1) lookups.

Memory Management:
Problem: How to handle big files.
Solution: The 'with open' was used in managing resources.

Performance Optimization:
Problem: How to assure efficiency in execution.
Solution: List comprehensions and efficient loops have been used.

## Future Improvement
Spell Suggestor: Facilities for auto-suggesting and spelling corrections of misspelled words in real time.
User Custom Dictionary: User will be allowed to insert his/her own custom words into the dictionary.
Contextual Analysis: Grammar and contextual checks will also be performed with the check to return more accurate results.
UI Interface: A graphical interface should be made for ease of usage.
Multiple Language Support: The system should provide support for various languages other than English.
Real-time Spell Check: Implement a text editor so that when an English text file is opened, it checks for errors in the document in real time.
Frequency Analysis: The system will keep statistics on the most common mistakes and frequently used words.
Synonym Suggestions: The software would be able to offer synonyms of words for vocabulary enrichment.

## Reference
1. https://youtu.be/htIAygIz_xU?si=yDScP1pnHEld0Xi9
2. https://youtu.be/_nkQd9SyEpw?si=usGZtycgsRZyPSNs
