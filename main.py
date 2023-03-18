from random import choice
import os

class Wordlee:
    def __init__(self):
        self.running = True
        self.options = [1,2,3,4,5,6,7]
        self.words = []
        length = int(input("Length of word: "))
        
        self.langs_available = {}
        for i, lang in enumerate(os.listdir('lang/')):
            self.langs_available[i] = lang
        lang_option = self.choose_lang()
        
        self.load_words(self.langs_available[lang_option], length)

    def run(self):
        while self.running:
            print("1) Exists letter and has a known position")
            print("2) Exists letter without a known position")
            print("3) Letter does not exists")
            print("4) Check remaining words")
            print("5) Random word")
            print("6) Exit game")
            
            option = input("Select an option: ")
            while ((not option.isdigit()) or (int(option) not in self.options)):
                print("Please, enter a valid option")
                option = input("Select an option: ")
            
            option = int(option)

            if option == 1:
                letter = input("Letter: ")
                posicion = int(input("Position: "))
                self.letter_and_position(letter, posicion)
                
            elif option == 2:
                letters = input("Letters (leave a blank space between each): ").split(' ')
                self.letter_without_position(letters)

            elif option == 3:
                letters = input("Letters (leave a blank space between each): ").split(' ')
                self.no_letter(letters)

            elif option == 4:
                print(self.words)
                print(len(self.words))

            elif option == 5:
                print(choice(self.words))
            
            elif option == 6:
                run = False

    def choose_lang (self):
        print("\nAvailable languajes")
        for i in self.langs_available:
            print(f"{i}) {self.langs_available[i]}")

        option = int(input("Select a languaje: "))
        print('\n')

        return option

    def letter_and_position(self, letra:str, posicion:int):
        palabras_aux = []
        for i in self.words:
            if letra != str(list(i)[posicion - 1]):
                palabras_aux.append(i)
        for _palabra in palabras_aux:
            self.words.remove(_palabra)
        print(f"Remaining words: {str(len(self.words))}. Discarded words: {str(len(palabras_aux))}")

    def letter_without_position(self, letras:list):
        palabras_aux = []
        for letra in letras:
            for palabra in self.words:
                if letra not in palabra:
                    palabras_aux.append(palabra)
        for _palabra in palabras_aux:
            self.words.remove(_palabra)
        print(f"Remaining words: {str(len(self.words))}. Discarded words: {str(len(palabras_aux))}")

    def no_letter(self, letras:list):
        palabras_aux = []
        for letra in letras:
            for palabra in self.words:
                if letra in palabra:
                    palabras_aux.append(palabra)
        for _palabra in palabras_aux:
            try:
                self.words.remove(_palabra)
            except:
                pass
        print(f"Remaining words: {str(len(self.words))}. Discarded words: {str(len(palabras_aux))}")

    def load_words(self, filename:str, length:int):
        f = open(f"lang/{filename}", "r")
        for line in f:
            if len(line.strip()) == length:
                self.words.append(line.strip())
        f.close()
        print(f"Loaded words: {str(len(self.words))}")


if __name__ == '__main__':
    Wordlee().run()