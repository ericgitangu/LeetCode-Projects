class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7:'pqrs', 8: 'tuv', 9: 'wxyz'}
        
        combinations, combination = [], []
        
        def dfs(curr_digit):
            if len(combination) == len(digits):
                combinations.append(''.join(list(combination)))
                return
            for digit in range(curr_digit, len(digits)):
                string = phone.get(int(digits[digit]))
                for char in string:
                    combination.append(char)
                    dfs(digit + 1)
                    combination.pop()
            return combinations
        
        return dfs(0)
            