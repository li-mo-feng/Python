for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a==b) or (b==c) or (a==c):
                pass
            else:
                print(a,b,c)