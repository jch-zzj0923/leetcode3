class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last={}
        for idx ,char in enumerate(s):
            last[char]=idx
        res=[]
        left=0
        right=0
        for i ,j in enumerate(s):
            right=max(right,last[j])
            if i==right:
                res.append(i-left+1)
                left=i+1
        return res
if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    solution = Solution()
    print(solution.partitionLabels(s))  # Output: [9, 7, 8]