from collections import deque
from models.board import Board
from models.dice import Dice
from models.player import Player

class Game :
    def __init__(self,players,board_size,dice_count):
        self.players = deque([Player(player) for player in players])
        self.dice = Dice(dice_count)
        self.board = Board(board_size)
        self.winner = None

    def check_winner(self,player) :
        return player.current_pos == self.board.size**2
    
    def play_turn(self):
        player_turn = self.players.popleft()
        roll_value = self.dice.roll_dice()
        new_position = player_turn.current_pos + roll_value
        if new_position < self.board.size **2 :
            new_row,new_col = self.board.convert_position_to_coordinate(new_position)
            cell = self.board.cells[new_row][new_col]
            if cell.jump :
                print(f"player name : {player_turn.player_id} jumped from {cell.jump.start} to {cell.jump.end}")
                new_position = cell.jump.end

            player_turn.current_pos = new_position
            print(f"{player_turn.player_id} is now at position {player_turn.current_pos}")

            if self.check_winner(player_turn) :
                self.winner = player_turn
        self.players.append(player_turn)

    def play_game(self):
        n = 5
        while not self.winner :
            self.play_turn()

        return self.winner


    
