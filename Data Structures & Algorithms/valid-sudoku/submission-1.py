class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = [[] for i in range(len(board))]
        boxes = [[] for i in range(len(board))]

        for i in range(len(board)):
            temp = []
            for j in range(len(board)):
                cell_value = board[i][j]
                if cell_value == ".": continue

                # Line check
                if cell_value in temp:
                    return False
                else: 
                    temp.append(cell_value)

                # Column check
                if cell_value in column[j]:
                    return False
                else: 
                    column[j].append(cell_value)

                # Box check
                a = int(j/3)
                b = int(i/3)
                box_idx = int(3 * b + a)
                if cell_value in boxes[box_idx]: 
                    return False
                else: 
                    boxes[box_idx].append(cell_value)

        return True
                

            
