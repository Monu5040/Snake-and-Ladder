
from models.game import Game

players_name = ["Monu","Aalok"]
board_size = 6
dice_count = 2
game = Game(players_name,board_size,dice_count)
game.board.set_jump(3,8)
game.board.set_jump(8,23)
game.board.set_jump(35,4)

print(game.play_game())



