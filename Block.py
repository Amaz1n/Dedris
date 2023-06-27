# Tetris block base class
class Block:
    shape = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    # Default 3x3 Types: L, T, J, S, Z
    # 2x2 Type: O
    # 4x4 Type: I
    def __init__(self, block_type=0):
        if block_type <= 4:
            if block_type <= 2:
                self.shape[0] = [1, 1, 1]
                self.shape[1][block_type] = 1
            elif block_type == 3:
                self.shape[0] = [0, 1, 1]
                self.shape[1] = [1, 1, 0]
            else:
                self.shape[0] = [1, 1, 0]
                self.shape[1] = [0, 1, 1]
        elif block_type == 5:  # O
            self.shape = [[1, 1], [1, 1]]
        else:  # I
            self.shape = [[0, 1, 0, 0],
                          [0, 1, 0, 0],
                          [0, 1, 0, 0],
                          [0, 1, 0, 0]]


    # Terminal print function for testing
    def print(self):
        print(self.shape[0])
        print(self.shape[1])
        print(self.shape[2])
        print("=========")

    # List rotation using zip from:
    # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    def rotate(self, clockwise=True):
        if clockwise:
            self.shape = list(map(list, zip(*self.shape[::-1])))
        else:
            self.shape = list(map(list, zip(*self.shape)))[::-1]

