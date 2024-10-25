for n in range(2, 101):
    premier = False
    i = 2
    while i < n and not premier :
        if n % i == 0 :
            premier = True
        i += 1
    if not premier :
        print(n)