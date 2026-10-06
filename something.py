def wizard(N,start,duels):
    owner = start
    changed_hand = 1
    for i in range(N):
        if duels[i][1] == owner:
            owner = duels[i][0]
        changed_hand += 1
    print(owner, changed_hand)
wizard(3, "A", ["BA", "CB", "DA"])
