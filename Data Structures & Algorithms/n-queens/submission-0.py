class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        pos_diag=set()
        neg_diag=set()
        board=[["."]* n for r in range(n)]
        result=[]
        def dfs(row):
            if row==n:
                copy=["".join(row) for row in board]
                result.append(copy)
            for c in range(n):
                if c in col or (row+c) in pos_diag or (row-c) in neg_diag:
                    continue
                col.add(c)
                pos_diag.add(row+c)
                neg_diag.add(row-c)
                board[row][c]="Q"
                dfs(row+1)
                col.remove(c)
                pos_diag.remove(row+c)
                neg_diag.remove(row-c)
                board[row][c]="."
        dfs(0)
        return result    