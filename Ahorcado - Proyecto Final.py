    # Hangman game in Python
# Author: Anthony Peñafiel
# This program applies conditionals, loops and basic string handling.

import os

def clear_screen():
    """Clear the console screen (works on Windows and Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")
    
import random

def choose_difficulty():
    """Ask the user to choose a difficulty and return: 'FACIL', 'NORMAL' or 'DIFICIL'."""
    while True:
        clear_screen()
        print("Elige una dificultad:")
        print("1) Fácil")
        print("2) Normal")
        print("3) Difícil")
        option = input("Opción (1/2/3): ").strip()

        if option == "1":
            return "FACIL"
        elif option == "2":
            return "NORMAL"
        elif option == "3":
            return "DIFICIL"
        else:
            input("Opción inválida. Presiona ENTER para intentar de nuevo...")

def get_word_bank():
    """Return the dictionary of words->hints for each difficulty."""
    return {
        "FACIL": {
            "GATO": "Animal doméstico común.",
            "CASA": "Lugar donde vives.",
            "SOL": "Estrella que ilumina la Tierra."
        },
        "NORMAL": {
            "PYTHON": "Lenguaje de programación.",
            "INTERNET": "Red global de comunicación.",
            "TECLADO": "Dispositivo para escribir en la computadora."
        },
        "DIFICIL": {
            "ALGORITMO": "Conjunto de pasos para resolver un problema.",
            "ENCRIPTACION": "Proceso para proteger información.",
            "MICROPROCESADOR": "Componente principal de cálculo en un computador."
        }
    }

def pre_game_dialog(hint):
    """Show pre-game dialogs inspired by MAS."""
    clear_screen()
    print("Pensaré en una palabra...")
    input("\nPresiona ENTER para continuar...")

    clear_screen()
    print("Muy bien, tengo una.")
    input("\nPresiona ENTER para continuar...")

    clear_screen()
    print("Pista:", hint)
    input("\nPresiona ENTER para comenzar el juego...")


def initialize_game(difficulty):
    """Initialize the main game variables based on difficulty."""
    word_bank = get_word_bank()[difficulty]       # dict palabra -> pista
    secret_word = random.choice(list(word_bank.keys())).upper()
    hint = word_bank[secret_word]                 # pista de esa palabra

    max_attempts = 6
    wrong_attempts = 0

    current_state = ["_" for _ in secret_word]
    guessed_letters = []

    return secret_word, hint, max_attempts, wrong_attempts, current_state, guessed_letters


def show_current_state(current_state, wrong_attempts, max_attempts, guessed_letters):
    """Show the current progress of the game to the user."""
    print("=== JUEGO DEL AHORCADO ===")
    print("Palabra: ", " ".join(current_state))
    print(f"Intentos incorrectos: {wrong_attempts} / {max_attempts}")
    print("Letras usadas: ", " ".join(guessed_letters))
    print()


def read_letter():
    """Read a letter OR special commands '?' (hint) and '!' (give up)."""
    while True:
        letter = input("Adivina una letra, escribe '?' para repetir la pista, '!' para rendirte: ").strip().upper()

        if letter in ("?", "!"):
            return letter
        elif len(letter) != 1:
            print("Por favor ingrese solo UNA letra (o '?' / '!').")
        elif not letter.isalpha():
            print("Por favor ingrese una letra válida (A-Z), o '?' / '!'.")
        else:
            return letter

def ask_play_again():
    """Ask the user if they want to play again. Returns True/False."""
    while True:
        answer = input("¿Te gustaría volver a jugar? (si/no): ").strip().lower()

        if answer in ("si", "sí", "s"):
            return True

        if answer in ("no", "n"):
            print("\nOkey. ¡Juguemos de nuevo pronto! 😊")
            input("Presiona ENTER para salir...")
            return False

        print("Respuesta inválida. Escribe 'si' o 'no'.")


def process_guess(secret_word, current_state, guessed_letters, letter):
    """
    Process the user's guess.
    Returns True if the letter is in the word, False otherwise.
    """
    # If the letter was already used, we inform the user
    if letter in guessed_letters:
        print("Ya usaste esa letra. Prueba con otra.")
        return None  # None = no penalty, no reward

    guessed_letters.append(letter)

    hit = False
    # We update all positions where the letter appears
    for index, char in enumerate(secret_word):
        if char == letter:
            current_state[index] = letter
            hit = True

    return hit


def is_game_won(current_state):
    """Check if the player has guessed all the letters."""
    return "_" not in current_state


def main():
    while True:
        difficulty = choose_difficulty()
        secret_word, hint, max_attempts, wrong_attempts, current_state, guessed_letters = initialize_game(difficulty)
        pre_game_dialog(hint)
        
        # Main game loop
        while wrong_attempts < max_attempts and not is_game_won(current_state):
            clear_screen()
            print(f"Dificultad: {difficulty}")
            show_current_state(current_state, wrong_attempts, max_attempts, guessed_letters)

            user_input = read_letter()

            if user_input == "?":
                print("Pista:", hint)
                input("\nPresiona ENTER para continuar...")
                continue

            if user_input == "!":
                print("Te rendiste. La palabra era:", secret_word)
                input("\nPresiona ENTER para salir...")
                return

            result = process_guess(secret_word, current_state, guessed_letters, user_input)

            if result is True:
                print("¡Buen trabajo! La letra está en la palabra.")
            elif result is False:
                print("Letra incorrecta.")
                wrong_attempts += 1

            input("\nPresiona ENTER para continuar...")

        # Fin de partida (ganó o perdió)
        clear_screen()
        print(f"Dificultad: {difficulty}")
        show_current_state(current_state, wrong_attempts, max_attempts, guessed_letters)

        if is_game_won(current_state):
            print("¡FELICIDADES! Adivinaste la palabra:", secret_word)
        else:
            print("JUEGO TERMINADO. La palabra era:", secret_word)

        if not ask_play_again():
            return


if __name__ == "__main__":
    main()
