for a in range(1, 1000):
    for b in range(a, 1000):
        for c in range(b, 1000):
            # Once we have an iteration of a, b, and c
            # Determine if it fits the criteria of a+b+c==1000 and
            #  a^2 + b^2 == c^2
            # Test a+b+c first because it is a faster test.  Takes ~half the time
            if (a + b + c == 1000):
                if (a * a + b * b == c * c):
                    # Print answers
                    print('A: ' + str(a) + ' B: ' + str(b) + ' C: ' + str(c))
                    print('Product is: ' + str(a * b * c))
                    # If we found it, exit to save time
                    exit()
