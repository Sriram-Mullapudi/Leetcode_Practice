import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort the events by start day
        events.sort()
        event_ptr = 0
        total_days = max(end for _, end in events)
        
        min_heap = []
        attended = 0

        for day in range(1, total_days + 1):
            # Step 2: Push all events starting today to the heap
            while event_ptr < len(events) and events[event_ptr][0] == day:
                heapq.heappush(min_heap, events[event_ptr][1])  # push endDay
                event_ptr += 1
            
            # Step 3: Remove events already expired (endDay < current day)
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            # Step 4: Attend the event that ends the earliest
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1

        return attended
