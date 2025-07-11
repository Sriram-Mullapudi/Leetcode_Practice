import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        # Min-heap of available room indices
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        
        # Min-heap of (end_time, room_index)
        busy_rooms = []
        
        # Count of meetings per room
        room_meeting_count = [0] * n
        
        for start, end in meetings:
            # Free up rooms that are available before current start
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room)
            
            duration = end - start
            
            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms, (end_time + duration, room))
            
            room_meeting_count[room] += 1
        
        # Return room with most meetings (tie => smallest index)
        max_meetings = max(room_meeting_count)
        for i in range(n):
            if room_meeting_count[i] == max_meetings:
                return i
