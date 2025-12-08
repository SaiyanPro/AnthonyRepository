# Hangman game in Python
# Author: Anthony Peñafiel
# This program applies conditionals, loops and basic string handling.

import os

def clear_screen():
    """Clear the console screen (works on Windows and Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")


def initialize_game():
    """Initialize the main game variables."""
    secret_word = "COMPUTADORA".upper()  # you can change this word
    max_attempts = 6
    wrong_attempts = 0

    # Create the initial state with underscores, e.g. "___________"
    current_state = ["_" for _ in secret_word]

    guessed_letters = []  # list to store already tried letters

    return secret_word, max_attempts, wrong_attempts, current_state, guessed_letters


def show_current_state(current_state, wrong_attempts, max_attempts, guessed_letters):
    """Show the current progress of the game to the user."""
    print("=== JUEGO DEL AHORCADO ===")
    print("Palabra: ", " ".join(current_state))
    print(f"Intentos incorrectos: {wrong_attempts} / {max_attempts}")
    print("Letras usadas: ", " ".join(guessed_letters))
    print()


def read_letter():
    """Read one letter from the user and validate the input."""
    while True:
        letter = input("Introduce una letra: ").strip().upper()

        if len(letter) != 1:
            print("Por favor ingrese solo UNA letra.")
        elif not letter.isalpha():
            print("Por favor ingrese una letra válida (A-Z).")
        else:
            return letter


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
    secret_word, max_attempts, wrong_attempts, current_state, guessed_letters = initialize_game()

    # Main game loop
    while wrong_attempts < max_attempts and not is_game_won(current_state):
        clear_screen()
        show_current_state(current_state, wrong_attempts, max_attempts, guessed_letters)
        letter = read_letter()

        result = process_guess(secret_word, current_state, guessed_letters, letter)

        if result is True:
            print("¡Buen trabajo! La letra está en la palabra.")
        elif result is False:
            print("Letra incorrecta.")
            wrong_attempts += 1

        input("\nPresiona ENTER para continuar...")

    clear_screen()
    show_current_state(current_state, wrong_attempts, max_attempts, guessed_letters)

    if is_game_won(current_state):
        print("¡FELICIDADES! Adivinaste la palabra:", secret_word)
    else:
        print("JUEGO TERMINADO. La palabra era:", secret_word)


if __name__ == "__main__":
    main()
