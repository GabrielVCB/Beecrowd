initial_hour, initial_minute, final_hour, final_minute = map(int, input().split())

if initial_hour == final_hour and initial_minute == final_minute:
  hours_time = 24
  minutes_time = 0
else:
  minutes_time = final_minute - initial_minute
  if initial_hour < final_hour or (initial_hour == final_hour and minutes_time >= 0):
    hours_time = final_hour - initial_hour
  else:
    hours_time = 24 - initial_hour + final_hour

  if minutes_time < 0:
    minutes_time += 60
    hours_time -= 1

print("O JOGO DUROU", hours_time, "HORA(S) E", minutes_time, "MINUTO(S)")