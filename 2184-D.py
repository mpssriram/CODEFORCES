t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    bob_wins = 0

    for x in range(1, n + 1):
        steps = x.bit_length() + x.bit_count() - 1
        if steps > k:
            bob_wins += 1

    print(bob_wins)
        
        