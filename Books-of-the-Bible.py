import random

word_list = ["genesis", "job", "exodus", "leviticus", "numbers", "deuteronomy", "joshua", "judges", "ruth", "samuel", "chronicles", "psalms", "proverbs", "ecclesiastes", "kings", "isaiah", "jeremiah", "lamentations", "hosea", "joel", "amos", "obadiah", "jonah", "micah", "nahum", "habakkuk", "zephaniah", "ezekiel", "daniel", "ezra", "esther", "nehemiah", "haggai", "zechariah", "malachi", "matthew", "mark", "luke", "john", "acts", "thessalonians", "corinthians", "galatians", "romans", "james", "colossians", "philemon", "ephesians", "philippians", "peter", "hebrews", "timothy", "titus", "jude", "revelation"]

chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")