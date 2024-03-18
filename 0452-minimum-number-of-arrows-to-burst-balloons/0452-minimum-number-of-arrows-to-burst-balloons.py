class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        end_boundry = points[0][1]
        arrows = 1
        for i in range(1,len(points)):
            if points[i][0] <= end_boundry:
                continue
            else:
                end_boundry = points[i][1]
                arrows += 1
        return arrows