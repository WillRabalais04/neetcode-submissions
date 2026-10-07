class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        flat = [num for row in matrix for num in row]
        def binarySearch(arr, target):
            if not arr:
                return False

            mp = len(arr) // 2

            if arr[mp] < target:
                return binarySearch(arr[mp + 1:], target)
            elif arr[mp] > target:
                return binarySearch(arr[:mp], target)
            else:
                return True
        print(flat)
        return binarySearch(flat,target)

            

        

        return True
    
        
