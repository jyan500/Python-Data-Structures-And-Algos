class SeatManager:
    import heapq
    def __init__(self, n: int):
        """
        https://leetcode.com/problems/seat-reservation-manager/
        available seats are 1 to n initially
        heap to receive the smallest numbered unreserved seat
        heappop() to reserve the lowest numbered seat
        when unreserving, push back into the queue

        Time Complexity: O(NLogN) to initialize, O(LogN) for reserve and unreserve
        Space: O(N)
        """
        self.unreserved = []
        self.n = n
        for i in range(self.n):
            heapq.heappush(self.unreserved, i+1)

    def reserve(self) -> int:
        """
        fetches smallest numbered unreserved seat
        """
        seat = heapq.heappop(self.unreserved)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        """
        unreserves the seat with given seat number
        """
        heapq.heappush(self.unreserved, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)