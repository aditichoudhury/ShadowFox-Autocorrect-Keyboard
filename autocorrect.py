from spellchecker import SpellChecker

# Initialize the spell checker
spell = SpellChecker()

# Take input from user
text = input("Enter your sentence: ")

# Split text into words
words = text.split()

corrected_text = []

# Check each word
for word in words:
    if word in spell:
        corrected_text.append(word)
    else:
        correction = spell.correction(word)
        print(f"'{word}' might be misspelled. Suggested: '{correction}'")
        corrected_text.append(correction)

# Output the corrected sentence
print("Corrected Sentence:", " ".join(corrected_text))
