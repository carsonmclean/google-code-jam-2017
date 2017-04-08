t = int(input())
for i in range(1, t+1):
    n = input()
    n_len = len(str(n))
    n = map(int, str(n))
    #print(n)
    #print(n_len)
    
    for j in range(n_len-1, 0, -1):
        if (n[j-1] > n[j]):
            #print(str(n[j-1]) + " is > than " + str(n[j]) + " and j = " + str(j))
            n[j-1] = n[j-1] -1
            k = j
            while k < n_len:
                n[k] = 9
                k += 1
        #print(n)
    #print(int(''.join(map(str, n))))
    n = int(''.join(map(str, n)))
    print "Case #{}: {}".format(i, n)   
    #print('\n\n\n')
