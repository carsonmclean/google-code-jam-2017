import Queue

t = int(input())
for i in range(1, t+1):
    n, k = [int(s) for s in raw_input().split(" ")]

    # Roughing out ideas...I didn't end up following this exactly in the end...
    # when doing small EGs by hand, gives a feel similar to a binary search
    # note that you pick the "center" of given extremes to be as far as possible from other occupied stalls
    # Note that there is a preference to pick left, meaning that on successive rounds, the right side will be as large or larger (depending on odd/even)
    # So, divide the range into two. The spot just left of center is used by the current customer.
    # Then, the spot just right of center serves as the left most extreme for the next customer. so, order is important

    # stack of pairs/tuples of ranges that are empty
    range_queue = Queue.PriorityQueue()

    # initialize the pairs with the range over the entire stalls
    range_queue.put(tuple((-(n+1), 0, n+1)))
    
    # simulate one less than actual visitors
    for j in range(k-1):

        sub_range = range_queue.get()
        average = (sub_range[2] + sub_range[1]) / 2 

        left_range = tuple((-(average-sub_range[1]), sub_range[1], average))
        right_range = tuple((-(sub_range[2]-average), average, sub_range[2]))

        range_queue.put(left_range) 
        range_queue.put(right_range) 

    # simulate the last visitor
    sub_range = range_queue.get()
    average = (sub_range[2] + sub_range[1]) / 2
    left_distance = abs(average - sub_range[1]) - 1
    right_distance = abs(sub_range[2] - average) - 1

    max_dist = max(left_distance, right_distance)
    min_dist = min(left_distance, right_distance)

    if k >= n:
        print "Case #{}: 0 0".format(i)
    else:
        print "Case #{}: {} {}".format(i, max_dist, min_dist)