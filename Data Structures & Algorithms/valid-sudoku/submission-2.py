class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = [set() for i in range(len(board))]
        boxes = [set() for i in range(len(board))]

        for i in range(len(board)):
            temp = set()
            for j in range(len(board)):
                cell_value = board[i][j]
                if cell_value == ".": continue

                # Line check
                if cell_value in temp:
                    return False
                else: 
                    temp.add(cell_value)

                # Column check
                if cell_value in column[j]:
                    return False
                else: 
                    column[j].add(cell_value)

                # Box check
                a = int(j/3)
                b = int(i/3)
                box_idx = int(3 * b + a)
                if cell_value in boxes[box_idx]: 
                    return False
                else: 
                    boxes[box_idx].add(cell_value)

        return True
                

            
