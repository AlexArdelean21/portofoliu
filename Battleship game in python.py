# Battle ship game
# Each player should have 3 ships, the ships should be of diffrent sizes. Ship A(5)"Carrier", ship B(4)"Battleship" and ship C(3)"Submarine". The player should be able to
#select where to place his ships on the map. The map is 10*10

# Create a 10x10 game board with '_' representing empty cells
game_board = [['_' for _ in range(10)] for _ in range(10)]

# Create the ship class 
class Ship:

    ships = {"A": 5, "B": 4, "C": 3}

    def __init__(self, type):
        self.type = self.ships[type]


# EXAMPLE OF SHIP PLACEMENT
# Place a battleship at coordinates (3, 4) to (3, 7)
for col in range(4, 7):
    game_board[3][col] = 'O'  # 'O' represents the battleship and '>' represents it's head
game_board[3][7] = '>'

for row in game_board:
    print(' '.join(row))
