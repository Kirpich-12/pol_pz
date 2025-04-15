class Marix4:
    def __init__(self, row1, row2, row3, row4):
        self.rows= (row1, row2, row3, row4)
    def determinant(self, a11, a12, a21, a22):
        det = a11*a22 - a12*a21 
        return det
    def minor2(self, row_index_1, row_index_2):
         

