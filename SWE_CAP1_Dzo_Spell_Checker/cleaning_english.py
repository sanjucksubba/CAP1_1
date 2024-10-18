import re

document_path = "dictionary (1).txt"
with open(document_path, "r", encoding="utf-8") as file:
  dictionary = file.read()  

old_dictionary = dictionary
updated_dictionary = dictionary

updated_dictionary = re.sub(r'\b[a-zA-Z]+\\b|\d+|^\w\s', '', updated_dictionary) 
with open(document_path, "w", encoding="utf-8") as file: 
    file.write(updated_dictionary)

print("All English words, Numbers and punctuation have been deleted from the file")
