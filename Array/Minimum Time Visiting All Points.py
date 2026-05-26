class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0
        for i in range(len(points)-1):
            x1= points[i][0]
            y1= points[i][1]
            x2= points[i+1][0]
            y2= points[i+1][1]
            x_diff= abs(x2-x1)
            y_diff= abs(y2-y1)
            ans+= max(x_diff,y_diff)
        return ans
