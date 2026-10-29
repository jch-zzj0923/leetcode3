class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        ans=[0]*n
        st=[]
        for i, t in enumerate(temperatures):
            while st and t> temperatures[st[-1]]:
                j=st.pop()
                ans[j]= i-j
            st.append(i)
        return ans        
if __name__=="__main__":
    s=Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))