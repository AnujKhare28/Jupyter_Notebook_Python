from spellchecker import Spellchecker

class SpellcheckerApp: 

    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self):
        words = text.split()
        corrected_words = []

        for word in words: 
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
               print(f"Corrected '{word}' to '{corrected_word}'")
               corrected_words.append(corrected_word)

               return ' '.join(corrected_words)

    def run(self):

        print("Welcome to the Spellchecker App!")

        while True:
            text = input("Enter text to check (or type 'exit' to quit): ")
            if text.lower() == 'exit':
                print("Exiting the Spellchecker App. Goodbye!")
                break

            corrected_text = self.correct_text()
            if corrected_text:
                print(f"Corrected Text: {corrected_text}")
            else:
                print("No corrections made.")


if __name__ == "__main__":
    app = SpellcheckerApp()
    app.run()