class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        for i in range(len(digits)-1, -1, -1):
            print(remainder)
            new_digit = digits[i] + remainder
            if new_digit < 10:
                digits[i] = new_digit
                return digits
            elif i != 0:
                digits[i] = int(new_digit % 1)
                remainder = new_digit // 10
            elif i == 0:
                digits[i] = int(new_digit % 1)
                remainder = new_digit // 10
                digits.insert(0, remainder)
                return digits
