class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        idx = len(digits) - 1
        while idx >= 0:
            if digits[idx] != 9:
                digits[idx] += 1
                break
            if idx == 0:
                digits[0] = 1
                digits.append(0)
                break
            digits[idx] = 0
            idx -= 1

        return digits