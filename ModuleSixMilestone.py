# David Vega
# Southern New Hampshire University
# IT-140 - Intro to Scripting


#  Below print statements print the heading of the game
print()
print('*' * 50)
print('         DRAGON TEXT ADVENTURE GAME')
print('Move commands: North, South, East, West, exit')
print('*' * 50)


def show_status(current_room):
    """ function definition that is passed parameter current_room and
    returns the players current location.
    """
    print('You are in the {}'.format(current_room))
    return current_room


def user_prompt():
    """ function definition that requests the user's next move
    and store in a variable which it returns
    """
    next_move = input("Enter next move: ")
    return next_move


def move_to_room(rooms, current_room, direction):
    """function definition that takes in (3) params "rooms, "current_room," and "direction."
    Funcs purpose is to move user between rooms.
    """
#  While loop runs the statements in its body while the current_room exists in the rooms dictionary.
    while current_room in rooms:
        print()  # Prints newline
        show_status(current_room)  # Func call to show current_room.
        next_move = user_prompt()  # Func call and assigns value to next_move.
        print()  # Prints newline
#  IF statement checks to see if next_move contains "exit" if so the loop breaks and the game ends.
        if next_move == 'exit':
            print('Thank you for playing! Goodbye.')
            break
#  IF statement checks to see if next_move is one of the rooms dictionary keys.
#  if so, it will assign current_room with the value of the key it found.
#  ELSE IF next_move is NOT in directions tuple, show "Invalid Entry" message to user.
#  ELSE show "You can't go that way." message to user
        if next_move in rooms[current_room]:
            current_room = rooms[current_room][next_move]
        elif next_move not in direction:
            print("Invalid Entry")
        else:
            print()
            print("You can\'t go that way.")
            print()


def main():
    """ Function definition for the entry point to the program.
    static local variables are defined here.
    """
    # A dictionary for the simplified dragon text game
    # The dictionary links a room to other rooms.
    rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'},
        'exit': None
    }

    directions = ('North', 'South', 'East', 'West', 'exit')
    current_room = 'Great Hall'
    # show_status(current_room)
    move_to_room(rooms, current_room, directions)


main()  # function call to begin the game. Main entry point of game play.
