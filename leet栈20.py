class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                st.append(i)
            elif i == ')':
                if not st or st.pop() != '(':
                    return False
            elif i == '}':
                if not st or st.pop() != '{':
                    return False
            elif i == ']':
                if not st or st.pop() != '[':
                    return False
        return len(st) == 0
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))  
