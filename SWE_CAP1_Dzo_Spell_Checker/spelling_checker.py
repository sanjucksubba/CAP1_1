with open("dictionary (1).txt", "r", encoding="utf-8") as one:
        dictionary = [word.strip() for word in one.readlines()]
        

with open("357.txt", "r", encoding="utf-8") as two:
         checker = two.readlines ()

for line_no, line in enumerate(checker, start=1):
    words_on_the_line = line.split ()
    for position_of_word, word in enumerate(words_on_the_line, start=1):
        if word not in dictionary:
            print(f"Word error: '{word}' at line number {line_no}, Position {position_of_word}")