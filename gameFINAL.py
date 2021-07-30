
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# ─██████──██████─██████████████─████████████████───██████████─██████████████─██████████████───██████─────────██████████████─██████████████─
# ─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─
# ─██░░██──██░░██─██░░██████░░██─██░░████████░░██───████░░████─██░░██████░░██─██░░██████░░██───██░░██─────────██░░██████████─██░░██████████─
# ─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██─────██░░██───██░░██──██░░██─██░░██──██░░██───██░░██─────────██░░██─────────██░░██─────────
# ─██░░██──██░░██─██░░██████░░██─██░░████████░░██─────██░░██───██░░██████░░██─██░░██████░░████─██░░██─────────██░░██████████─██░░██████████─
# ─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██─────██░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─
# ─██░░██──██░░██─██░░██████░░██─██░░██████░░████─────██░░██───██░░██████░░██─██░░████████░░██─██░░██─────────██░░██████████─██████████░░██─
# ─██░░░░██░░░░██─██░░██──██░░██─██░░██──██░░██───────██░░██───██░░██──██░░██─██░░██────██░░██─██░░██─────────██░░██─────────────────██░░██─
# ─████░░░░░░████─██░░██──██░░██─██░░██──██░░██████─████░░████─██░░██──██░░██─██░░████████░░██─██░░██████████─██░░██████████─██████████░░██─
# ───████░░████───██░░██──██░░██─██░░██──██░░░░░░██─██░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
# ─────██████─────██████──██████─██████──██████████─██████████─██████──██████─████████████████─██████████████─██████████████─██████████████─
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
#Variable for testing purposes, set to false here so that it will be changed when the code starts, and even if that is later deleted this will remain
# so that it does not cause errors:
debug = True

#This is where text colours are stored.
class text_colors:
    RED = '\033[91m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    GRAY = '\033[90m'
    ENDC = '\033[0m'

#This is where information about the character will be stored
class character:
    name = ""
    occupation = None

#This is where the comparisons occupations will be stored
class occ:
    soldier = "SOLDIER"
    scientist = "SCIENTIST"

mother_names = [
    "Morgana Lewis",
    "Grace Johnson",
    "Zara Johnson",
    "Emma John",
    "Katherine Clark",
    "Natalya Richmond",
    "Arianna Justice",
    "Piper Clay",
    "Sierra Barnes",
    "Jayde Hutchinson"]

#This is where story variables are stored
class story:
    gun = False
    medicine = False
    trust = False
    mother = None
    child = None
    mother_alive = True

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# ─██████─────────██████████─██████████████───████████████████───██████████████─████████████████───██████████─██████████████─██████████████─
# ─██░░██─────────██░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
# ─██░░██─────────████░░████─██░░██████░░██───██░░████████░░██───██░░██████░░██─██░░████████░░██───████░░████─██░░██████████─██░░██████████─
# ─██░░██───────────██░░██───██░░██──██░░██───██░░██────██░░██───██░░██──██░░██─██░░██────██░░██─────██░░██───██░░██─────────██░░██─────────
# ─██░░██───────────██░░██───██░░██████░░████─██░░████████░░██───██░░██████░░██─██░░████████░░██─────██░░██───██░░██████████─██░░██████████─
# ─██░░██───────────██░░██───██░░░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██─────██░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─
# ─██░░██───────────██░░██───██░░████████░░██─██░░██████░░████───██░░██████░░██─██░░██████░░████─────██░░██───██░░██████████─██████████░░██─
# ─██░░██───────────██░░██───██░░██────██░░██─██░░██──██░░██─────██░░██──██░░██─██░░██──██░░██───────██░░██───██░░██─────────────────██░░██─
# ─██░░██████████─████░░████─██░░████████░░██─██░░██──██░░██████─██░░██──██░░██─██░░██──██░░██████─████░░████─██░░██████████─██████████░░██─
# ─██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░░░██─██░░██──██░░░░░░██─██░░██──██░░██─██░░██──██░░░░░░██─██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
# ─██████████████─██████████─████████████████─██████──██████████─██████──██████─██████──██████████─██████████─██████████████─██████████████─
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# Import libraries here:
import time, random, sys, getpass
from types import new_class
from typing import Collection

# ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# ─██████████████─██████──██████─██████──────────██████─██████████████─██████████████─██████████─██████████████─██████──────────██████─██████████████─
# ─██░░░░░░░░░░██─██░░██──██░░██─██░░██████████──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░██─██░░██████████──██░░██─██░░░░░░░░░░██─
# ─██░░██████████─██░░██──██░░██─██░░░░░░░░░░██──██░░██─██░░██████████─██████░░██████─████░░████─██░░██████░░██─██░░░░░░░░░░██──██░░██─██░░██████████─
# ─██░░██─────────██░░██──██░░██─██░░██████░░██──██░░██─██░░██─────────────██░░██───────██░░██───██░░██──██░░██─██░░██████░░██──██░░██─██░░██─────────
# ─██░░██████████─██░░██──██░░██─██░░██──██░░██──██░░██─██░░██─────────────██░░██───────██░░██───██░░██──██░░██─██░░██──██░░██──██░░██─██░░██████████─
# ─██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██──██░░██─██░░██─────────────██░░██───────██░░██───██░░██──██░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██─
# ─██░░██████████─██░░██──██░░██─██░░██──██░░██──██░░██─██░░██─────────────██░░██───────██░░██───██░░██──██░░██─██░░██──██░░██──██░░██─██████████░░██─
# ─██░░██─────────██░░██──██░░██─██░░██──██░░██████░░██─██░░██─────────────██░░██───────██░░██───██░░██──██░░██─██░░██──██░░██████░░██─────────██░░██─
# ─██░░██─────────██░░██████░░██─██░░██──██░░░░░░░░░░██─██░░██████████─────██░░██─────████░░████─██░░██████░░██─██░░██──██░░░░░░░░░░██─██████████░░██─
# ─██░░██─────────██░░░░░░░░░░██─██░░██──██████████░░██─██░░░░░░░░░░██─────██░░██─────██░░░░░░██─██░░░░░░░░░░██─██░░██──██████████░░██─██░░░░░░░░░░██─
# ─██████─────────██████████████─██████──────────██████─██████████████─────██████─────██████████─██████████████─██████──────────██████─██████████████─
# ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

def game_reset(death = True):
    if death:   
        user_input = input("You have died, would you like to try again? [Y/N] \n\t")
    else:
        user_input = input("You have completed the game, would you like to play again for another outcome? [Y/N]\n\t")

    if user_input.upper() == "Y":
        #Reset variables:
        character.occupation = None
        character.name = None
        story.gun = False
        story.medicine = False
        story.mother = None
        story.child = None
        story.mother_alive = True

        #Starts the story from scratch:
        hospital_room()
    elif user_input.upper() == "N":
        #Closes the program
        typewrite(f"{text_colors.RED}Better luck next time\nThanks for playing{text_colors.ENDC}")
        time.sleep(3)
        sys.exit()
    else:
        typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")
        if death:
            game_reset()
        else:
            game_reset(False)

#This creates a loop in which it iterates over the message, and sleeps for a short duration before typing the next character, providing a typewriter aesthetic
def typewrite(message, delay_between_char = 0.01):
    """This will take a provided message, and a supplied time (in seconds) which it will wait for between typing letters"""
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_between_char)
    #Print an empty line to reduce the need for \n after every typewrite()
    print()

#This allows us to create formatting gaps in the game, without them suddenly appearing from nowhere, instead panning the previous text away
def next_section(lines: int, time_per_line: float, pause: bool = False):
    """This will take the number of lines, and the time per line given and run a loop to print empty lines. The pause parameter defaults
    Example usage for between two sections: next_section(4, 0.25)
    This would run this function to print 4 lines with 0.25s between each for a total of 1 second """
    if pause:
        time.sleep(2)
    for i in range(lines):
        time.sleep(time_per_line)
        print()

#chance(80, character.occupation, occ.scientist)
#This allows us to implement a way to randomly decide if a character manages to succeed in their goal.
def chance(number_to_pass: int, occupation: str, beneficial_occupation: str):
    """This will take the number designated at the challenge, the character occupation, and the occupation that would have the edge for this challenge, and return True or False, 
    depending on if they have succeeded the roll."""
    roll = random.randint(1, 100)
    
    if occupation == beneficial_occupation:
        roll += 40

    if roll >= number_to_pass:
        return True
    else:
        return False
# chance(40, character.occupation, occ.soldier)



# ────────────────────────────────────────────────────────────────────────
# ─██████████████─██████████─██████████████─██████─────────██████████████─
# ─██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─
# ─██████░░██████─████░░████─██████░░██████─██░░██─────────██░░██████████─
# ─────██░░██───────██░░██───────██░░██─────██░░██─────────██░░██─────────
# ─────██░░██───────██░░██───────██░░██─────██░░██─────────██░░██████████─
# ─────██░░██───────██░░██───────██░░██─────██░░██─────────██░░░░░░░░░░██─
# ─────██░░██───────██░░██───────██░░██─────██░░██─────────██░░██████████─
# ─────██░░██───────██░░██───────██░░██─────██░░██─────────██░░██─────────
# ─────██░░██─────████░░████─────██░░██─────██░░██████████─██░░██████████─
# ─────██░░██─────██░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██─
# ─────██████─────██████████─────██████─────██████████████─██████████████─
# ────────────────────────────────────────────────────────────────────────
def title():
    """This will print the title screen."""
    if debug ==True:
        print("title()")

    print(f"""{text_colors.GREEN}WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNKOOXWWWWWWWWWWWWWWWMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWW0:...c0NXWWWWWWWWWWWWWWWWWWWWMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX:     .,'dNWWWWWWWWWWWWWWWWWMMWWWWWWWWWWWWWWWWWWMMMWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWMWWWWWWWWWWWWMMMWWK;        ;KWWWWWWWWWWWMMWWWWWWWWWWWWWWWWWWWWWWWWMMMWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMNl        .kWWWWWWWWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMMx.      ,xXMMMWWWWWWMMWWWWWWWWWWWWWWWWWWWWWWMMWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMWWMk.      :XWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWMMWWWWWWWWWWWWWWWWWWWWWWMMMWWWd.      :XMWWWWWWWWWWMMWMWWWWWWWMMWWWMMWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWO'       .:oxO0KKXXK0kdodk0KXNNNNXXXXXNWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWMMWWWWWWWMXo.             ....'..     ..,,,''''..',:cokKNWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWMMMWWWWWWWNc      ..                .......     .''..   .lXMWWWWWWWWWWWWWWWWWWW
    MMWWWWWMMWWWWWWWWWWWWMMMMWMMWWM0'                ..,:lokOOOOOkkxl. .;xXXKk;...'OMWWWWWWWWWWWWWWWMMMM
    WWWWWWWWWWWWWWWWWWWWWWWMMWMMWWM0'                   .':cldkOKNWWWd.;KWWWWWx::;cOMWWWWWWWWWWWWWWWMMWW
    WWWWWWWWWWWWWWWWWWWWWWWMMWMMWWMK;             .        ......';cxKllNWMWWW0xOOOXWWWWWWWWWWWWWWWWWWWW
    MMWWWWWWWWWMMWWWWWWWWWWMMWMMWWMNl             'ddc:'  .xKKo...  .d0XWWWWWWWNWWWWMWWWWWWWWWWWWWWWWWWW
    MWWWWWWWWWWWMWWWWWWWWWWWWWWWWWMWo.            .OWWWK: ,0WW0,ldol,oKWMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWWWMMWWWMWo             :KWWMWl.lNWWNkkkOXkOWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWMMMWWWWWWWWWWWWWWWWMMMWWWMWo            .kWWWMNl:KWWWWWWNNWWWMWWWWWMWMMMMWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWMMMMWWWMWo         .. ,0WWWWNKXMMWWMWWWWWWMWWWMWWWWWWMMWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWNNWWWMMMMWWWMMMd      ..... ,0WWMMMMWWMWWMWWWWWWWMWWMMWWWWWWWWWMMWMWNNWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWNXNWMMWWWWWWMMMWo   ......   .OMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWNXNWWWWWWWWWWWW
    WWWWWWWWWWWWWWWMWWWMMWMMWWWWMMMWl  .....     .dWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWMMWWWMMWWWWMMMNc             ,0WWWWWWWWWWWMMMWWWWWWWWWWWWWWWWWWWWWWMMMWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWMMWMWWWWMWWX;              ;0WMWWWWWWWWWMMWWWWWWWWWWWWWWWWWWWWMMWWMMWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWWMMWWWWWK,               'kXNWMWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    MWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMk.        .'.     ..:kNMWWWWWWWWWWWWWWWWWWWWWWWWMMWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWMWWWWWMX:         ,Ok:.      .cKWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWMMWWWWWWWWWMWWWWWWWWMMWWXl.        .oNWW0o'      ,OWMWWMWMMWWWWWWWWMMMWWWWWMMWWWWWMMWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWMMWWWWO'        .cXWWWWWK;      .xWMMWWMWWWWWMMWWWWWWWWWWMMWWWWWMMWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWW0'       .lXWWWWWWWd....   .dWWWWWWWWWWMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWMWWWWWW0,       ,0NNWWWMWWx;lo,    .kWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWMMWWWWk.       ,KMWWWWMMWdxNXc    .dWWWWWWMWWWWWWMMMMWWWWWWWWWWWWWWWWWWWWWMWW
    WWWWWWWWWWWWWWWWWWWWWWWWWMWWK:        ;KMWWWWWMWKXMWo    .xMWWMWWWWWWWWWMMWWWWWWWWWWWWWWWWWWWWWWMMMW
    WWWWWWWWWWWWWWWWWWWWWWWMMWW0;         ,KMWWMMWWMWWM0'    .kMWWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWMWNx.      .ldcoXMWWMMWWWW0x:     ,KWWMWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWMXo. .     ,0MWWWWWWMMWWKl....    :XWWWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWMMWWWWWMNklc:;,.  :XMWWWWWWWWWWd. ...... 'OWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWMMWWMWWWW0c'''oK0xcxNWWWWWWWWWWWKd,....,lookXWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWMMWWWW0c'....dNWWWWWWWWWWWWWWWWMO.     ....'kWMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWK;    .oXWWWWWWMWWWWWWMMMWM0l:::::::::cOWNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWMWXkdoldKWWWWWWWWWWWWWWWMMMWWMMWWWMMMWWMWWWNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWMMMMWWWWMWWMWWWWWWWWWWWWWWWWWMMWWWWWWWWWMWMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW{text_colors.ENDC}
    {text_colors.RED}
    ██╗███████╗  ██╗████████╗██╗░██████╗  ████████╗██╗░░██╗███████╗
    ██║██╔════╝  ██║╚══██╔══╝╚█║██╔════╝  ╚══██╔══╝██║░░██║██╔════╝
    ██║█████╗░░  ██║░░░██║░░░░╚╝╚█████╗░  ░░░██║░░░███████║█████╗░░
    ██║██╔══╝░░  ██║░░░██║░░░░░░░╚═══██╗  ░░░██║░░░██╔══██║██╔══╝░░
    ██║██║░░░░░  ██║░░░██║░░░░░░██████╔╝  ░░░██║░░░██║░░██║███████╗
    ╚═╝╚═╝░░░░░  ╚═╝░░░╚═╝░░░░░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

    ██╗░░░░░░█████╗░░██████╗████████╗  ████████╗██╗░░██╗██╗███╗░░██╗░██████╗░  ██╗  ██████╗░░█████╗░
    ██║░░░░░██╔══██╗██╔════╝╚══██╔══╝  ╚══██╔══╝██║░░██║██║████╗░██║██╔════╝░  ██║  ██╔══██╗██╔══██╗
    ██║░░░░░███████║╚█████╗░░░░██║░░░  ░░░██║░░░███████║██║██╔██╗██║██║░░██╗░  ██║  ██║░░██║██║░░██║
    ██║░░░░░██╔══██║░╚═══██╗░░░██║░░░  ░░░██║░░░██╔══██║██║██║╚████║██║░░╚██╗  ██║  ██║░░██║██║░░██║
    ███████╗██║░░██║██████╔╝░░░██║░░░  ░░░██║░░░██║░░██║██║██║░╚███║╚██████╔╝  ██║  ██████╔╝╚█████╔╝
    ╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝  ╚═════╝░░╚════╝░{text_colors.ENDC}{text_colors.GRAY}
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗
    ╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝
    ██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗██████╗
    ╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝╚═════╝
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{text_colors.ENDC}{text_colors.RED}

    ▒█▀▀█ ▒█▀▀▀ ▒█▀▀▄ ░█▀█░ 　 ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀▄ ▒█░▒█ ▒█▀▀█ ▀▀█▀▀ ▀█▀ ▒█▀▀▀█ ▒█▄░▒█ ▒█▀▀▀█ 
    ▒█▄▄▀ ▒█▀▀▀ ▒█░▒█ █▄▄█▄ 　 ▒█▄▄█ ▒█▄▄▀ ▒█░░▒█ ▒█░▒█ ▒█░▒█ ▒█░░░ ░▒█░░ ▒█░ ▒█░░▒█ ▒█▒█▒█ ░▀▀▀▄▄ 
    ▒█░▒█ ▒█▄▄▄ ▒█▄▄▀ ░░░█░ 　 ▒█░░░ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄▀ ░▀▄▄▀ ▒█▄▄█ ░▒█░░ ▄█▄ ▒█▄▄▄█ ▒█░░▀█ ▒█▄▄▄█{text_colors.ENDC} """)


# ───────────────────────────────────────────────────────────────────────────────
# ─██████████████─██████████████─████████████████───██████████████────████████───
# ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██────██░░░░██───
# ─██░░██████░░██─██░░██████░░██─██░░████████░░██───██████░░██████────████░░██───
# ─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───────██░░██──────────██░░██───
# ─██░░██████░░██─██░░██████░░██─██░░████████░░██───────██░░██──────────██░░██───
# ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───────██░░██──────────██░░██───
# ─██░░██████████─██░░██████░░██─██░░██████░░████───────██░░██──────────██░░██───
# ─██░░██─────────██░░██──██░░██─██░░██──██░░██─────────██░░██──────────██░░██───
# ─██░░██─────────██░░██──██░░██─██░░██──██░░██████─────██░░██────────████░░████─
# ─██░░██─────────██░░██──██░░██─██░░██──██░░░░░░██─────██░░██────────██░░░░░░██─
# ─██████─────────██████──██████─██████──██████████─────██████────────██████████─
# ───────────────────────────────────────────────────────────────────────────────

#This scene will result in the player choosing a name and occupation, there is no way to fail out of this section
def hospital_room():
    """This is the first scene that we will call, it allows the user to set their name, and calls a function to allow them to set their occupation. Afterwards it will move them to hospital_corridor()"""
    #debug code
    if debug == True:
        print("hospital_room()")
    
    #type scenario
    typewrite(f"{text_colors.PURPLE}\nYou awake in an unfamiliar room at first dazed and confused. You begin to look around as your eyes adjust and find yourself waking in a hospital room. You then begin to get up and pull yourself out of bed and move over to thechart hanging off the end to check your details...{text_colors.ENDC}", 0.001)

    #wait half a second
    time.sleep(0.5)
    
    #continue typing
    typewrite(f"{text_colors.PURPLE}As you read your chart you hear a groaning noise, almost as if another patient was on their deathbed...{text_colors.ENDC}")

    #print two lines
    next_section(2, 0.2)

    #Asks the player to insert their name and sets it in the character class
    character.name = input(f"{text_colors.PURPLE}On the chart you see your name...{text_colors.ENDC} \n{text_colors.CYAN}Who are you?{text_colors.ENDC}\n" )
    
    #print two lines
    next_section(2, 0.2)

    #Calls get_occupation() in order to set the character occupation
    character.occupation = get_occupation()

    #print two lines
    next_section(2, 0.1)

    #Calls hospital_corridor() in order to progress
    hospital_corridor()

def get_occupation():
    """This will be called by hospital_room() a single time, in order to set the players occupation"""

    #debug code
    if debug == True:
        print("get_occupation()")

    #take user input
    user_input = input(f"{text_colors.PURPLE}That's right, you're {character.name}, and you were:{text_colors.CYAN} \nA:{text_colors.ENDC} A soldier {text_colors.CYAN} \nB:{text_colors.ENDC} A scientist {text_colors.ENDC}\n\t")

    #if user_input is valid, choose an occupation based on input and return it to hospital_room(), otherwise try again.
    if user_input.upper() == "A" or user_input.upper() == "SOLDIER":
        typewrite(f"{text_colors.GREEN}it's all coming back to you now, you were a Soldier.{text_colors.ENDC}")
        return "SOLDIER"
    if user_input.upper() == "B" or user_input.upper() == "SCIENTIST":
        typewrite(f"{text_colors.GREEN}it's all coming back to you now, you were a Scientist.{text_colors.ENDC}")
        return "SCIENTIST"
    else:
        typewrite(f"{text_colors.RED}Unrecognised input, please try again: {text_colors.ENDC}")
        character.occupation = get_occupation()

#This scene presents the player with their second meaningful choice, and the first chance of failure. it is intended to show that there is still a chance when taking a gamble on a choice.
def hospital_corridor():
    """This is the second scene, a hospital corridor, this will allow the user their first choice that can result in death."""
    #debug code
    if debug == True:
        print("hospital_corridor()")

    #write scenario
    typewrite(f"{text_colors.PURPLE}Making your way out of the room into the corridor and you turn to the right to begin walking down the corridor lights flickering with dark spots around as others are broken. You come to a set of double doors and move through them to find a way down the stairs or use the elevator. Now you must choose how you wanna leave…{text_colors.ENDC}\n")

    #Checks if the character is set as a soldier, if they are, provide them with a slightly different input prompt, to indicate their success chance
    if character.occupation == occ.soldier:
        user_input = input(f"You take the \n{text_colors.CYAN} A:{text_colors.ENDC} Stairs \n {text_colors.CYAN}B:{text_colors.ENDC} Elevator (80% Chance of success)\n\t")
    else:
        user_input = input(f"You take the \n{text_colors.CYAN} A:{text_colors.ENDC} Stairs \n {text_colors.CYAN}B:{text_colors.ENDC} Elevator (40% Chance of success){text_colors.ENDC}\n\t")
    
    #Checks the characters input from the previous input, and checks that it is valid, if it is valid and leads to the elevator, they will have an encounter with a zombie.
    #if it is vaild, and leads to the stairs, it will lead to the hospital foyer
    if user_input.upper() == "A" or user_input.upper() == "STAIRS":
        next_section(2, 0.2)
        typewrite(f"{text_colors.GREEN}You cautiously make your way down the stairs, the groaning getting quieter as you do{text_colors.ENDC}")
        
        hospital_foyer()

    #if it is valid, and leads to the elevator it will give the player a chance to succeed, depending on their occupation.
    elif user_input.upper() == "B" or user_input.upper() == "ELEVATOR":
        if character.occupation == occ.soldier:
            #if the character is a soldier, they are provided with an increased chance of success in this scenario, otherwise they are less likely to survive.
            if chance(60, character.occupation, occ.soldier): #80% chance of success
                typewrite(f"{text_colors.GREEN}You approach the elevator, the groaning grows louder. You prepare yourself and press the call button and watch as the doors open, freeing a corpse that lurches towards you, teeth gnashing.\nYou manage to avoid its bite, and shove it to the ground, before quickly stamping on its head, crushing it. \nYou board the elevator and press the button for the ground floor, and breathe heavily as the elevator springs into action.{text_colors.ENDC}")

                #Prints 2 empty lines to provide an easy to read format
                next_section(2, 0.1)

                #Moves to the hospital foyer
                hospital_foyer()
            else:
                typewrite(f"{text_colors.RED}As you approach the elevator, the groaning grows louder. You press the call button and watch as the doors open, and a corpse flies out and tries to bites you. While you avoid the first attempt, it manages drags you to the floor and starts to rip off your flesh and eat it.{text_colors.ENDC}")      
                
 
                #Prints 2 empty lines to provide an easy to read format
                next_section(2, 0.1)
                
                typewrite(f"\t\t\t\t\t{text_colors.RED}GAME OVER{text_colors.ENDC}", 0.3)
                
                #Offer the player a chance to try again.
                game_reset()          
        else:
            if chance(60, character.occupation, occ.soldier): #40% chance of success
                typewrite(f"{text_colors.GREEN}As you approach the elevator, the groaning grows louder. You prepare yourself and press the call button and watch as the doors open, freeing a corpse that lurches towards you, teeth gnashing.\n You manage to avoid its bite, and shove it to the ground before getting into the elevator and slamming the door close button, watching it disappear behind the sliding doors. \nYou press the button for the ground floor, and breathe heavily as the elevator springs into action.{text_colors.ENDC}")
 
                #Prints 2 empty lines to provide an easy to read format
                next_section(2, 0.1)

                #Move the player to the hospital_foyer()
                hospital_foyer()
            else:
                typewrite(f"{text_colors.RED}As you approach the elevator, the groaning grows louder. You nervously press the call button and watch as the doors open, and a corpse flies out and bites you. it drags you to the floor and starts to rip off your flesh and eat it.{text_colors.ENDC}")

                #Prints 2 empty lines to provide an easy to read format
                next_section(2, 0.1)

                typewrite(f"\t\t\t\t\t{text_colors.RED}GAME OVER{text_colors.ENDC}", 0.3)
                #Offer the player a chance to try again.
                game_reset()

    #if input is NOT valid, it will re-call this function to loop back to the beginning       
    else: 
        typewrite(f"{text_colors.RED}Unrecognised input, please try again: {text_colors.ENDC}")
        hospital_corridor()
    


def hospital_foyer():
    """This is the third scene of part 1, and allows the player to make a mistake, by not searching for supplies."""
    #debug code
    if debug == True:
        print("hospital_foyer()")
    #Provide player with an idea of the scene.
    typewrite(f"{text_colors.PURPLE}You now find yourself downstairs in the main foyer and as you scan the bodied riddled room filled with decomposing smelly husks about the place. You then notice a radio on the ground attached to a dead police officer. You hear a broadcast on repeat:{text_colors.ENDC} {text_colors.GREEN}“there is a safe place north of the town”{text_colors.ENDC} {text_colors.PURPLE}")
    
    #print two lines
    next_section(2, 0.2)

    #print character action
    typewrite(f"{text_colors.PURPLE}You pick up the radio and put it in your pocket.{text_colors.ENDC}")
    
    #Take user input 
    user_input = input(f"do you: \n{text_colors.CYAN}A:{text_colors.ENDC} Search for supplies \n{text_colors.CYAN}B:{text_colors.ENDC} leave the hospital? \n\t")

    #if the user input is valid, then provide them with the appropriate option, otherwise repeat this function
    if user_input.upper() == "A" or user_input.upper() == "SEARCH":
        #Set variables indicating that the hospital was looted
        story.gun = True
        story.medicine = True
        
        #formatting
        next_section(2, 0.2)

        #Print outcome:
        typewrite(f"{text_colors.GREEN}You decide to take a look around for some supplies, it seems like you might need them... \n\nYou check around the police officer and manage to find his gun, luckily still loaded.\nAfterwards, you decide to hop the counter into the pharmacy and manage to find a backpack with some medical supplies loaded into it.{text_colors.ENDC}")
        
        #Move to next section
        car_park()
    elif user_input.upper() == "B" or user_input.upper() == "LEAVE":
        #formatting
        next_section(2, 0.2)
        #Print outcome
        typewrite(f"{text_colors.GREEN}You decide that it isn't worth the risk of hanging around, and start to leave the hospital.{text_colors.ENDC}")

        #Move to next section
        car_park()
    else:
        #Print error message
        typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")
        
        #Clear some space for formatting
        next_section(2, 0.1)
        
        #Restart section
        hospital_foyer()
    

def car_park():
    "This is the final scene of act 2: where one of the players choices will effect whether they can proceed or not."
    
    #debug code
    if debug == True:
        print("car_park()")

    #Print scenario:
    typewrite(f"{text_colors.PURPLE}On your way to the hospital car park you see more bodies idly wandering around and cars in various states of disrepair but you see one that looks like It’s in good condition. While walking up to it, you notice there’s also a dirt track/path you can walk through down to get away.{text_colors.ENDC}")

    #Formatting:
    next_section(2, 0.2)

    #Take user input
    user_input = input(f"Which do you choose? \n{text_colors.CYAN}A:{text_colors.ENDC} The car \n{text_colors.CYAN}B:{text_colors.ENDC} The dirt track\n\t")
    
    #if user input valid, progress. otherwise fail
    if user_input.upper() == "A" or user_input.upper() == "CAR":
        if character.occupation == occ.soldier and story.gun == True or character.occupation == occ.scientist:
            next_section(2, 0.2)
            if character.occupation == occ.soldier:
                typewrite(f"{text_colors.GREEN}You get into the car and try to hotwire it, only for it to struggle, and make a racket, attracting a couple of zombies, you manage to loose a few shots from your new pistol while trying to start the car. \n\nYou manage to hold them off long enough to get the car started, and speed off down the road.{text_colors.ENDC}")
            else:
                typewrite(f"{text_colors.GREEN}As you get into the car you begin to hotwire it, taking care to keep quiet lest you attract the corpses. \n\nYou manage to get the car running quickly without making much noise, and you start to slowly drive out of the car park.{text_colors.ENDC}")
            
            #You see a zombie walking towards you as you go to start the car, you use your gun and drive away safely")
            car_journey()
        else:
            #formatting
            next_section(2, 0.2)

            #print output.
            typewrite(f"{text_colors.RED}You begin trying to hotwire the car, struggling as you do so, and the car starts sputtering. You curse as a group of zombies turn, attracted by the noise of the car. \n\nWithout a weapon you can't hope to take on this many.{text_colors.ENDC}")

            #game over text
            typewrite(f"\t\t\t\t\t{text_colors.RED}GAME OVER{text_colors.ENDC}", 0.3)

            #reset variables
            game_reset()
    elif user_input.upper() == "B" or user_input.upper() == "ROAD":
        #formatting: 
        next_section(2, 0.2)
        
        #print character action
        typewrite(f"{text_colors.RED}You take the path. it's quiet at first then you come down to a pack of zombies on a small bridge over a fast running river so you try to move around them slowly and start climb the side...\n\n Sadly, you fail to keep hold of the bridge, and slip into the river below, never to be seen again{text_colors.ENDC}")
        
        #game over text 
        typewrite(f"\t\t\t\t\t{text_colors.RED}GAME OVER{text_colors.ENDC}", 0.3)

        #reset variables
        game_reset()
    else:
        #print error
        typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")

        #restart section
        car_park()

# ───────────────────────────────────────────────────────────────────────────────────
# ─██████████████─██████████████─████████████████───██████████████────██████████████─
# ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██────██░░░░░░░░░░██─
# ─██░░██████░░██─██░░██████░░██─██░░████████░░██───██████░░██████────██████████░░██─
# ─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───────██░░██────────────────██░░██─
# ─██░░██████░░██─██░░██████░░██─██░░████████░░██───────██░░██────────██████████░░██─
# ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───────██░░██────────██░░░░░░░░░░██─
# ─██░░██████████─██░░██████░░██─██░░██████░░████───────██░░██────────██░░██████████─
# ─██░░██─────────██░░██──██░░██─██░░██──██░░██─────────██░░██────────██░░██─────────
# ─██░░██─────────██░░██──██░░██─██░░██──██░░██████─────██░░██────────██░░██████████─
# ─██░░██─────────██░░██──██░░██─██░░██──██░░░░░░██─────██░░██────────██░░░░░░░░░░██─
# ─██████─────────██████──██████─██████──██████████─────██████────────██████████████─
# ───────────────────────────────────────────────────────────────────────────────────

def car_journey():
    """The first scene of act 2, where the player will have a choice to try and rescue a mother and her child"""
    #debug code
    if debug == True:
        print("car_journey()")
    #Chooses a random name from a list of 10 for the mothers name, as long as one has not already been set
    if story.mother == None:
        story.mother = random.choice(mother_names)

    #print scenario
    typewrite(f"{text_colors.PURPLE}\n\nAs you drive down a classic small highway trees either side of you, with some crashed cars and destroyed cars all over the place on and off the road. As you keep driving you notice a mother and child off to the side of the road. {text_colors.ENDC}")
    
    #Takes the user input
    user_input = input(f"{text_colors.PURPLE}You can either pull over or drive on, what will you do?. {text_colors.ENDC}\nDo you: \n{text_colors.CYAN}A: {text_colors.ENDC}Pick them up \n{text_colors.CYAN}B:{text_colors.ENDC} Drive on \n\t")


    #Checks if the user input is valid, and sends them off to another function depending on what it is.
    if user_input.upper() == "A" or user_input.upper() == "STOP":
        #formatting
        next_section(2, 0.2)

        #action
        typewrite(f"{text_colors.GREEN}You pull over to the side of the road to pick up the mother, daughter pair, before setting off again{text_colors.ENDC}")

        #nect section
        car_journey_continued()
    elif user_input.upper() == "B" or user_input.upper() == "DRIVE":
         #formatting
         next_section(2, 0.2)

         #action
         typewrite(f"{text_colors.RED}You choose to ignore them and drive on and continue to the safe house the radio message mentioned. When you get there you find it overrun with zombies, that just heard the car coming. it's at this point the car decides to stop due to a lack of fuel. The zombies swarm your car before you can react pulling you out and ripping you limb from limb.{text_colors.ENDC}")
         
         #game over text
         typewrite(f"\t\t\t\t\t{text_colors.RED}GAME OVER{text_colors.ENDC}", 0.3)

         #reset variables
         game_reset()
    else:
        #formatting
        next_section(2, 0.2)

        #error
        typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")  
        
        #restart section
        car_journey()


def car_journey_continued():
    """Second scene of act 2, where the child begins to turn, and the player needs to have made a certain decision back in the hospital"""
    #debug code
    if debug == True:
        print("car_journey_continued()")

    #scenario
    typewrite(f"{text_colors.PURPLE}The mother introduces herself as {story.mother}, you start discussing the message being played over the radio and that you feel that’s the best way to go. However the {story.mother} says that there is a better way to survive and a better place to be picked up. You ask her how they came to be by the side of the road?\nShe explains that they both were running from a small group of zombies as they were searching for supplies themselves and they were caught off guard. They had made a run for it through the city and ended up in the woods nearby, and after finding the main road nearby, they we hoping to find someone or something.\nSome time later the girl starts to moan and groan and the mother reaches back to check to only discover that she has been bitten on her arm. {story.mother} asks if there’s anything you can do to help. {text_colors.ENDC}\n\nWhat do you do?")
    
    #formatting
    next_section(2, 0.2)

    if character.occupation == occ.scientist and story.medicine == True:
        #take user input
        user_input = input(f"{text_colors.PURPLE}You have to choose now if you want to provide medicine to slow the infection or keep it. Do you \n{text_colors.CYAN}A:{text_colors.ENDC} hand them over \n{text_colors.CYAN}B:{text_colors.ENDC} keep silent \n\t")
        #check user input
        if user_input.upper() == "A":
            #formatting
            next_section(2, 0.2)
            #action
            typewrite(f"{text_colors.GREEN}You pull the car over and administer the medicine, it seems that the symptoms have subsided for now...{text_colors.ENDC}")

            #Set the trust variable to true, to indicate the mother trusts you more
            story.trust = True

            #next section
            gas_station()
        elif user_input.upper() == "B":    
            #formatting
            next_section(2, 0.2)

            #action
            typewrite(f"{text_colors.GREEN}You choose to stay quiet and say we will try to find something soon to help with the symptoms.\nWho knows, you may need it later{text_colors.ENDC}")

            #progress
            gas_station()    
        else:
            #formatting
            next_section(2, 0.2)

            #error
            typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")

            #restart section
            car_journey_continued()

    elif character.occupation == occ.scientist and story.medicine == False:
        #Give option to improvise medicine or do nothing
        #This will use the chance() function
        user_input = input(f"You have to choose now if you want to improvise a remedy to slow the infection or keep it. Do you \n{text_colors.CYAN}A:{text_colors.ENDC} Try to improvise a solution \n{text_colors.CYAN}B:{text_colors.ENDC} Keep silent \n\t")
        if user_input.upper() == "A" or user_input.upper() == "IMPROVISE":
        # Brief description on what is happening that happens for both success and failure
            typewrite(f"{text_colors.GREEN}You pull the car over and improvise a remedy to see if you can slow the infection.{text_colors.ENDC}")
            if chance(80, character.occupation, occ.scientist): #This is the success condition
                #Print the flavour text for how the character succeeds
                typewrite(f"{text_colors.GREEN}\nYou find some basic medical supplies in the glovebox and improvise, managing to stave off the infection for now... You also notice that there is a gun, hidden away.{text_colors.ENDC}")
                story.gun = True
                
                #Formatting
                next_section(2, 0.2)

                #Set the trust variable to true, to indicate the mother trusts you more
                story.trust = True
                
                #Move to the gas station
                gas_station()
            else: #failure
                #Brief description on attempting to improvise something, finding no supplies and the child turning into a zombie and biting you
                typewrite(f"{text_colors.RED}\nYou pull over the car and start desperately searching through the car to try and find something to help you improvise a remedy but cannot find anything.\n As you search you hear the mother scream, and turn to see her child, now turned, scrambling at you, before biting your arm. \nIt's over, you're doomed.{text_colors.ENDC}")

                next_section(2, 0.2)

                typewrite(f"\t\t\t\t\t{text_colors.RED}GAME OVER{text_colors.ENDC}", 0.3)
                #call the game_reset() function
                game_reset()
        elif user_input.upper() == "B" or user_input.upper() == "KEEP":    
            typewrite(f"{text_colors.GREEN}You choose to stay quiet and say we will try to find something soon to help with the symptoms.\nWho knows, you may need it later{text_colors.ENDC}")
            
            next_section(2, 0.2)
            
            gas_station()    
        else:
            typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")
            car_journey_continued()

    elif character.occupation == occ.soldier and story.medicine == True:
        #Give option to give medicine or keep it
        user_input = input(f"{text_colors.PURPLE}You have to choose now if you want to try and help or keep the medicine.{text_colors.ENDC} \nDo you \n{text_colors.CYAN}A:{text_colors.ENDC} Try and help \n{text_colors.CYAN}B:{text_colors.ENDC} keep silent ")
        if user_input.upper() == "A":
            
            typewrite(f"{text_colors.GREEN}You pull the car over and administer the medicine and it seems to work.{text_colors.ENDC}")
            
            #Set the trust variable to true, to indicate the mother trusts you more
            story.trust = True
            
            next_section(2, 0.2)

            #Move on to the gas station
            gas_station()
        elif user_input.upper() == "B":    
            #Move onto the gas station
            typewrite(f"{text_colors.GREEN}You choose to stay quiet and say we will try to find something soon to help with the symptoms.\nWho knows, you may need it later{text_colors.ENDC}")

            next_section(2, 0.2)

            gas_station()    
        else:
            typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")
            car_journey_continued()
        return                   
    else:
         #character.occupation == occ.soldier and story.medicine == False: << This is just show that it will still run this line but it isn't needed to be there as per the else: will do it anyway.
        #Give option to improvide medicine or do nothing
        user_input = input(f"{text_colors.PURPLE}You have to choose now if you want to try and help or not.{text_colors.PURPLE} \nDo you \n{text_colors.CYAN}A:{text_colors.ENDC} Try and help \n{text_colors.CYAN}B:{text_colors.ENDC} keep silent \n\t")
        if user_input.upper() == "A":
            #Brief description on what is happening that happens for both success and failure
            typewrite(f"{text_colors.GREEN}You pull the car over and improvise a remedy to see if you can slow the infection.{text_colors.ENDC}")
            if chance(80, character.occupation, occ.scientist): #This is the success condition
                #Print the flavour text for how the character succeeds
                typewrite(f"{text_colors.GREEN}\nYou find some basic medical supplies in the glovebox and improvise, managing to stave off the infection for now...{text_colors.ENDC}")
                
                #Formatting
                next_section(2, 0.2)

                #Set the trust variable to true, to indicate the mother trusts you more
                story.trust = True
                
                #Move to the gas station
                gas_station()
            else: #failure
                #Brief description on attempting to improvise something, finding no supplies and the child turning into a zombie and biting you
                typewrite(f"{text_colors.RED}\nYou pull over the car and start desperately searching through the car to try and find something to help you improvise a remedy but cannot find anything.\n As you search you hear the mother scream, and turn to see her child, now turned, scrambling at you, before biting your arm. \nIt's over, you're doomed.{text_colors.ENDC}")
                
                next_section(2, 0.2)
                
                typewrite(f"\t\t\t\t\t{text_colors.RED}GAME OVER\n{text_colors.ENDC}", 0.3)
                
                next_section(2, 0.2)

                game_reset()
        elif user_input.upper() == "B":    
            typewrite(f"{text_colors.GREEN}You choose to stay quiet and say we will try to find something soon to help with the symptoms.\nWho knows, you may need it later{text_colors.ENDC}")
            
            next_section(2, 0.2)

            gas_station()
        else:
            typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")
            car_journey_continued()
        return    


        
def gas_station():
    """This is the final scene of act 2, where regardless of prior actions, the child will turn. There is no cure. The mother will ask for you to put down her child because she can't bring herself to do it"""

    if debug == True:
        print("gas_station()")

    typewrite(f"{text_colors.PURPLE}You reach a gas station and you find a good place there to hunker down for the night.\nThen unfortunately you wake the next morning to find the daughter has turned into a zombie. Then {story.mother} asks you to help her {text_colors.ENDC}")
    user_input = input(f"Do you \n{text_colors.CYAN}A:{text_colors.ENDC} convince her to put her daughter to rest \n{text_colors.CYAN}B:{text_colors.ENDC} Do it yourself \n\t")
    if story.trust == True:
        
        #if you have given her the medicine
        if user_input.upper() == "A":
            if story.trust:
                #action
                typewrite(f"{text_colors.GREEN}You manage to convince the mother that she should be the one to put the daughter to rest, and hand her the gun you found earlier.. She asks you for a moment alone, as you leave you hear sobbing followed by a gunshot... followed by another one... and no more sobbing \nAfter a moment, you decide to leave, fearing that the noise may attract the hoards{text_colors.ENDC}")    

                #set mother_alive variable
                story.mother_alive = False

                #formatting
                next_section(2, 0.2)

                #next section
                chopper_escape()
        elif user_input.upper() == "B": 
            #action   
            typewrite(f"{text_colors.GREEN}You act fast and grab the gun to shoot the daughter the mother understands you had no choice and that you need to leave.\nSo you both get up and leave on foot as there’s no time to get back to the car as the gunshot has attracted a hoard of zombies.{text_colors.ENDC}")
            
            #formatting
            next_section(2, 0.2)

            #next section
            chopper_escape()   
        else:
            #error
            typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")

            #restart sectton
            gas_station()

    else:
        if user_input.upper() == "A":
            #action
            typewrite(f"{text_colors.RED}You tell the mother she should be the one to put her her daughter to rest. \nAs you rummage through the bag to retrieve the gun and pass it to her, she notices the medicine you have stowed there and in a fit of rage she takes the gun shoots you. Moments later you hear another gunshot, and another... then everything goes dark...{text_colors.ENDC}")

            #formatting
            next_section(2, 0.2)
            
            #game over text
            typewrite(f"\t\t\t\t\t{text_colors.RED}GAME OVER{text_colors.ENDC}", 0.3)

            #restart story
            game_reset()
        elif user_input.upper() == "B":
            #action
            typewrite(f"{text_colors.GREEN}She takes the gun out of the bag and ask you to leave her alone for a moment, as you leave you hear sobbing followed by a gunshot... followed by another one... and no more sobbing \nAfter a moment, you decide to leave, fearing that the noise may attract the hoards.{text_colors.ENDC}")

            #set mother_alive to false
            story.mother_alive = False

            #formatting
            next_section(2, 0.2)

            #next section
            chopper_escape()
        else:
            #error
            typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")
            
            #restart section
            gas_station()


# ───────────────────────────────────────────────────────────────────────────────────
# ─██████████████─██████████████─████████████████───██████████████────██████████████─
# ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██────██░░░░░░░░░░██─
# ─██░░██████░░██─██░░██████░░██─██░░████████░░██───██████░░██████────██████████░░██─
# ─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───────██░░██────────────────██░░██─
# ─██░░██████░░██─██░░██████░░██─██░░████████░░██───────██░░██────────██████████░░██─
# ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───────██░░██────────██░░░░░░░░░░██─
# ─██░░██████████─██░░██████░░██─██░░██████░░████───────██░░██────────██████████░░██─
# ─██░░██─────────██░░██──██░░██─██░░██──██░░██─────────██░░██────────────────██░░██─
# ─██░░██─────────██░░██──██░░██─██░░██──██░░██████─────██░░██────────██████████░░██─
# ─██░░██─────────██░░██──██░░██─██░░██──██░░░░░░██─────██░░██────────██░░░░░░░░░░██─
# ─██████─────────██████──██████─██████──██████████─────██████────────██████████████─
# ───────────────────────────────────────────────────────────────────────────────────
  
def chopper_escape():
    """Final section"""
    #debug code
    if debug == True:
        print("chopper_escape()")
    
    #scenario
    typewrite(f"{text_colors.PURPLE}You continue down the road towards the radio tower and encounter a large zombie{text_colors.ENDC}")

    #user input
    if character.occupation == occ.soldier:
        user_input = input(f"Do you \n{text_colors.CYAN}A:{text_colors.ENDC} Try and attack the zombie \n{text_colors.CYAN}B:{text_colors.ENDC} Try and sneak around \n\t") 
    elif character.occupation == occ.scientist and story.mother_alive == True:
        user_input = input(f"Do you \n{text_colors.CYAN}A:{text_colors.ENDC} Try and attack the zombie (20% Chance) \n{text_colors.CYAN}B:{text_colors.ENDC} Try and sneak around \n\t") 
    else:
        user_input = input(f"Do you \n{text_colors.CYAN}A:{text_colors.ENDC} Try and attack the zombie \n{text_colors.CYAN}B:{text_colors.ENDC} Try and sneak around \n\t") 



    #if scientist + mother is alive
    if character.occupation == occ.scientist and story.mother_alive == True:
        #Tried to attack:
        if user_input.upper() == "A":
            #action
            typewrite(f"{text_colors.GREEN}You try and attack the zombie... {text_colors.ENDC}")
            if chance(80, character.occupation, occ.soldier): 
                #action
                typewrite(f"\n{text_colors.GREEN}By sheer luck and the power of a gun you manage to kill the zombie, unfortunately, {story.mother} was not quite so lucky, and was caught by one of its attacks, and has perished.{text_colors.ENDC}")

                #set mother_alive to False
                story.mother_alive = False

                #formatting
                next_section(2, 0.2)

                #next section
                radio_tower()
            else:
                #action
                typewrite(f"\n{text_colors.RED}You try to attack this monstrosity but very quickly as you begin to try this “thing” charges at you and with one massive sweep with It’s massive right arm it smacks you flying into the air like a ragdoll off into the woods.{text_colors.ENDC}")

                #formatting
                next_section(2, 0.2)

                #game over text
                typewrite(f"\t\t\t\t\t{text_colors.RED}GAME OVER{text_colors.ENDC}", 0.3)   

                #reset story:
                game_reset()
        elif user_input.upper() == "B":
            #action
            typewrite(f"{text_colors.GREEN}You grab {story.mother} and guide her over to slip down past the huge zombie and go over a dried up river and then continue on to the radio tower.{text_colors.ENDC}")

            #formatting 
            next_section(2, 0.2)

            #next section
            radio_tower()
        else:
            #error text
            typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")

            #restart section
            chopper_escape()

    elif character.occupation == occ.soldier and story.mother_alive == True:
        
        if user_input.upper() == "A":
            #action
            typewrite(f"{text_colors.GREEN}You attack the zombie, using your military training you manage to beat it, though {story.mother} dies in the struggle {text_colors.ENDC}") 
            
            #formatting 
            next_section(2, 0.2)

            #set mother_alive variable to False
            story.mother_alive = False

            radio_tower()
        elif user_input.upper() == "B":
            #action
            typewrite(f"{text_colors.GREEN}You grab {story.mother} and guide her over to slip down past the huge zombie and go over a dried up river and then continue on to the radio tower.{text_colors.ENDC}")

            #formatting
            next_section(2, 0.2)

            #next section
            radio_tower()
        else:
            #error text
            typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")

            #restart section
            chopper_escape()
    
    else: #mother.alive == False
    
        if user_input.upper() == "A":
            #action
            typewrite(f"{text_colors.RED}You try to attack this monstrosity but very quickly as you begin to try this “thing” charges at you and with one massive sweep with It’s massive right arm it smacks you flying into the air like a ragdoll off into the woods.{text_colors.ENDC}")

            #formatting
            next_section(2, 0.2)
            
            #Game over text
            typewrite(f"\t\t\t\t\t{text_colors.RED}GAME OVER{text_colors.ENDC}", 0.3)

            #restart game
            game_reset()

        elif user_input.upper() == "B":
            #action 
            typewrite(f"{text_colors.GREEN}You manage to sneak past{text_colors.ENDC}")
            
            #formatting
            next_section(2, 0.2)
            
            #next section()
            radio_tower()
        else:
            #error
            typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")
            
            #formatting
            next_section(2, 0.2)

            #restart section
            chopper_escape()
        
def radio_tower():
    #debug code:
    if debug:
        print("radio_tower()")
    if story.mother_alive == True:
        typewrite(f"{text_colors.PURPLE}You've made it to the radio tower, the mother enters the code which allows the helicopter pilot to find you much sooner than before.\nAs this happens a massive swarm of zombies starts rushing towards you, trying to break into the room.\nAs you both try to escape {story.mother} gets trapped in a room with a grated floor.{text_colors.ENDC}")
        
        user_input = input(f"Do you \n{text_colors.CYAN}A:{text_colors.ENDC} Go back and save her \n{text_colors.CYAN}B:{text_colors.ENDC} Escape without her \n\t") 

        if user_input.upper() == "A":
            #action
            typewrite(f"{text_colors.GREEN}You go to free her and she gets up and you tell her to run and get to the choppa.\nAs she does you turn around and a swarm of the undead envelops you and drag you down to the floor and finish you off. \n\nBut she gets away and lives as she is able to escape{text_colors.ENDC}")
            
            #formatting
            next_section(2, 0.2)

            #outcome
            typewrite(f"{text_colors.GREEN}You may have died, but you managed to save {story.mother}... Maybe that's enough...{text_colors.ENDC}")

            #formatting
            next_section(2, 0.2)

            #restart game:
            game_reset(False)
        elif user_input.upper() == "B":
            #action
            typewrite(f"{text_colors.GREEN}You look back at her but you take a moment before choosing to save yourself, turning around to run.\nAs you start to run it weighs on your mind what you have done. As you reach the stop of the stairs and run to the helicopter and climb in and it takes off you look back at the build and think…. \n\nDid I do the right thing in the end.{text_colors.ENDC}")

            #formatting
            next_section(2, 0.2)

            #outcome
            typewrite(f"{text_colors.GREEN}As the helicopter flies you away to some unknown place you consider your actions to this point. Was it worth it? Sacrificing someone for your own survival, in a world crippled by this pandemic...{text_colors.ENDC}")

            #formatting
            next_section(2, 0.2)

            #restart game
            game_reset(False)
        else:
            #error
            typewrite(f"{text_colors.RED}Unrecognised input, please try again:{text_colors.ENDC}")
            
            #formatting
            next_section(2, 0.2)

            #restart section
            radio_tower()
    
    
    else:
        #action
        typewrite(f"{text_colors.RED}You journey is nearly complete, but at what cost? In the distance you see the radio tower. You activate the signal but without a boost the chopper will take twice as long to find you. As soon as you enter the code a swarm of zombies begins to decend upon you. You're doomed...\n{text_colors.ENDC}")
        
        #game over text
        typewrite(f"\t\t\t\t\t{text_colors.RED}GAME OVER{text_colors.ENDC}", 0.3)
        
        #formatting
        next_section(2, 0.2)

        #restart game
        game_reset()
    


# ──────────────────────────────────────────────────────────
# ─████████████████───██████──██████─██████──────────██████─
# ─██░░░░░░░░░░░░██───██░░██──██░░██─██░░██████████──██░░██─
# ─██░░████████░░██───██░░██──██░░██─██░░░░░░░░░░██──██░░██─
# ─██░░██────██░░██───██░░██──██░░██─██░░██████░░██──██░░██─
# ─██░░████████░░██───██░░██──██░░██─██░░██──██░░██──██░░██─
# ─██░░░░░░░░░░░░██───██░░██──██░░██─██░░██──██░░██──██░░██─
# ─██░░██████░░████───██░░██──██░░██─██░░██──██░░██──██░░██─
# ─██░░██──██░░██─────██░░██──██░░██─██░░██──██░░██████░░██─
# ─██░░██──██░░██████─██░░██████░░██─██░░██──██░░░░░░░░░░██─
# ─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░██──██████████░░██─
# ─██████──██████████─██████████████─██████──────────██████─
# ──────────────────────────────────────────────────────────
         
title()

# This allows us to wait for input, while hiding what a player types.
getpass.getpass(f"\t\t\t\t\t{text_colors.GREEN}Press Enter to Begin{text_colors.ENDC}")

# Pans the title screen up, to hide the ascii art zombie.
next_section(37, 0.01, True)

#Begins the game properly
hospital_room()