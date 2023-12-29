from models.cells import Cell
from models.snake_or_ladder import SnakeOrLadder
class Board :
    def __init__(self,size) :
        self.size = size
        self.cells = [[Cell(i*size+j+1) for j in range(size)] for i in range(size)]

    def set_jump(self,start,end):
        start_row,start_col = self.convert_position_to_coordinate(start)
        end_row,end_col = self.convert_position_to_coordinate(end)
        self.cells[start_row][start_col].jump = SnakeOrLadder(start,end)
    
    def convert_position_to_coordinate(self,pos) :
        row = pos // self.size
        col = pos % self.size
        return row,col-1
    
   
    

    