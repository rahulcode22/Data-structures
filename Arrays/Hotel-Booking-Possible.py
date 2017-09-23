"""A hotel manager has to process N advance bookings of rooms for the next season.
His hotel has K rooms. Bookings contain an arrival date and a departure date.
He wants to find out whether there are enough rooms in the hotel to satisfy the demand.
Write a program that solves this problem in time O(N log N) ."""
def hotelBooking(arrival,depart,k):
    events = [(t,1) for t in arrival] + [(t,0) for t in depart]
    events.sort()
    guests = 0
    for event in events:
        if event[1] == 1:
            guests +=1
        else:
            guests -=1
        if guests > k:
            return 0
    return 1

arrival = [1,3,5]
depart = [2,6,8]
k=1
print hotelBooking(arrival,depart,k)
