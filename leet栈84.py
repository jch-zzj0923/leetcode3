class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        st=[]
        max_size=0
        heights.append(0)
        for l,h in enumerate(heights):
            while st and h<heights[st[-1]]:
                cur_idx=st.pop()
                cur_h=heights[cur_idx]
                left=st[-1] if st else -1
                wihth=l-left-1
                cur_size=wihth*cur_h
                if cur_size>max_size:
                    max_size=cur_size
            st.append(l)
        return max_size
if __name__=="__main__":
    s=Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))
