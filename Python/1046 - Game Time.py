start, end = map(int, input().split())

if start < end:
    game_time = end - start
elif start == end:
    game_time = 24
else:
    game_time = 24 - start + end

print("O JOGO DUROU", game_time, "HORA(S)")