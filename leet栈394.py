class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        n = len(s)
        for i in range(n):
            ch = s[i]
            if ch != ']':
                st.append(ch)
            else:
                cur = ""
                while st[-1] != '[':
                    cur = st.pop() + cur
                st.pop() 
                k = ""
                while st and st[-1].isdigit():
                    k = st.pop() + k
                cur = cur * int(k)
                for c in cur:
                    st.append(c)
        return "".join(st)
if __name__ == "__main__":
    s = "3[a]2[bc]"
    solution = Solution()
    result = solution.decodeString(s)
    print(result)  