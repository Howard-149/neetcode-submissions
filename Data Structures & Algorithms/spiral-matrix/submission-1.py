class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        l,r,t,b = 0,n-1,0,m-1
        ans = []
        while l<=r and t<=b:
            for j in range(l,r+1):
                ans.append(matrix[t][j])
            t+=1
            if t>b:
                break
            for i in range(t,b+1):
                ans.append(matrix[i][r])
            r-=1
            if r<l:
                break
            for j in range(r,l-1,-1):
                ans.append(matrix[b][j])
            b-=1
            if t>b:
                break
            for i in range(b,t-1,-1):
                ans.append(matrix[i][l])
            l+=1
        return ans
        
