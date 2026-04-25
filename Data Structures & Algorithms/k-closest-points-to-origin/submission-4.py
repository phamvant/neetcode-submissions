class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        ret = []

        for point in points:
            dis = point[0] ** 2 + point[1] ** 2
            heapq.heappush(maxHeap, [dis, point[0], point[1]])

        while k:
            dis, x, y = heapq.heappop(maxHeap)
            ret.append([x, y])
            k -= 1

        return ret