import heapq
def solution(book_time):
    answer = 0
    for i in range(len(book_time)):
        start, end = book_time[i]
        sh, sm = map(int, start.split(':'))
        eh, em = map(int, end.split(':'))
        start = sh*60+sm
        end = eh*60+em+10
        book_time[i] = [start, end]
    book_time = sorted(book_time, key=lambda x: x[0])
    
    rooms = []
    max_rooms = 0

    for start, end in book_time:
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
            
        heapq.heappush(rooms, end)
        max_rooms = max(max_rooms, len(rooms))

    answer = max_rooms
    return answer