class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        
        words = dict()
        lengths = dict()
        
        for i in range(len(s)):
            for j in range(len(s) -1, -1, -1):
                if s[i] != s[j]:
                    continue
                else:
                    if (s[i], s[j]) in lengths:
                        length = lengths.get((s[i], s[j]))
                        if j - i < length:
                            break
                    string = ''
                    tmp_i, tmp_j = i, j
                    flag = True
                    while tmp_i <= tmp_j: 
                        if s[tmp_i] != s[tmp_j]:
                            flag = False
                            break
                        tmp_i += 1
                        tmp_j -= 1

                    if flag:
                        lengths[(s[i], s[j])] = int(j - i)
                        words[s[i:j + 1]] = (j - i) + 1
                        break
        try:
            longest = max(words.values())
        except:
            pass
        
        for key, value in words.items():
            if value == longest:
                return key
        