class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        lx = 0
        n = len(s)

        m_len = 0 

        for i in reversed(range(n)):

            if s[i].isalpha():
                m_len+=1

                if i > 0 and s[i-1] == ' ':
                    break
        
        return m_len


        