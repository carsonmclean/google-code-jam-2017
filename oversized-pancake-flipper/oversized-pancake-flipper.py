t = int(input())
for i in range(1, t+1):
    s, k = [s for s in raw_input().split(" ")]
    k = int(k)
    s = list(s)

    total = 0

    # start on the left end and works towards right
    # keep flipping, so long as we can fit the paddle size k
    while (len(s) >= k):
        # ignore immediate pancakes that are + side up
        while True:
            if (len(s) > 0) and s[0] == '+':
                s = s[1:]
            else:
                break

        # check again if the paddle fits in the remaining pancakes
        if (len(s) >= k):
            # it flips, we've found a '-', going to flip
            total += 1
            # flipper loop, toggle k pancakes forward
            for j in range(k):
                if s[j] == '-':
                    s[j] = '+'
                else:
                    s[j] = '-'

    if (len(s) == 0):
        print "Case #{}: {}".format(i, total)
    else:
        print "Case #{}: IMPOSSIBLE".format(i)

