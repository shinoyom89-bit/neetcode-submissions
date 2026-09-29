class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if target > matrix[mid][-1]:
                left = mid + 1

            elif target < matrix[mid][0]:
                right = mid - 1

            else:
                row = mid
                break
        else:
            return False

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] > target:
                right = mid - 1

            elif matrix[row][mid] < target:
                left = mid + 1

            else:
                return True

        return False