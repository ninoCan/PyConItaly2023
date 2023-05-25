from enum import IntEnum, auto
import random

class Actions(IntEnum):
    ROCK = auto()
    PAPER = auto()
    SCISSOR = auto()
    LIZARD = auto()
    SPOCK = auto()

def main():
    while True:
        user = get_user_selection()
        computer = get_pc_selection()
        decide_winner(user, computer)

if __name__ == "__main__":
    main()
