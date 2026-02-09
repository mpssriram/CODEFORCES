t = int(input())

for _ in range(t):

    n, x, y = map(int, input().split())

    arr = list(map(int, input().split()))



    total_moves = 0

    for val in arr:

        total_moves += val // x



    max_money = 0

    for val in arr:

        current_moves = val // x

        incoming_moves = total_moves - current_moves

        amount = val + (incoming_moves * y)

        max_money = max(amount,max_money)



    print(max_money)






    

    