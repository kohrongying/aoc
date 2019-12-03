guards = {}

import time
from datetime import datetime 

def sort_file(file):
  f = open(file, 'r')
  time_list = f.readlines()
  time_list.sort(key=lambda date: datetime.strptime(date.split(']')[0][1:], "%Y-%m-%d %H:%M"))
  # sorted((time.strptime(d.split(']')[0][1:], "%Y-%m-%d %H:%M") for d in time_list), reverse=True)
  # print(time_list)
  return time_list

# sort_file('day42.txt')

def parse_file(file):  
  sorted = sort_file(file)

  for line in sorted:
    time, action = line.split(']')
    time = time[1:]
    date, timestamp = time.split(' ')
    year, month, day = date.split('-')
    hour, min = timestamp.split(':')
    action_words = action.strip().split(' ')

    if action_words[0] == "Guard":
      current_guard = action_words[1][1:]
    elif action_words[0] == "falls":
      current_sleep_start = min
    else:
      sleep_time = [current_sleep_start, min]
      if int(min) < int(current_sleep_start):
        sleep_duration = 60 - int(current_sleep_start) + int(min)
      else:
        sleep_duration = int(min) - int(current_sleep_start)
      if current_guard in guards:
        if "{}-{}".format(month, day) in guards[current_guard]["duty"]:
          guards[current_guard]["duty"]["{}-{}".format(month, day)].append(sleep_time)
        else: 
          guards[current_guard]["duty"]["{}-{}".format(month, day)] = [sleep_time]
      else:
        guards[current_guard]={"total_asleep":0, "duty": {"{}-{}".format(month, day):[sleep_time]}}
      guards[current_guard]['total_asleep']+= sleep_duration

def get_sleep_beauty():
  duration = 0
  sleeping_beauty = ""
  for key in guards:
    if guards[key]["total_asleep"] > duration:
      duration = guards[key]["total_asleep"]
      sleeping_beauty = key
  
  return sleeping_beauty 

def get_total_sleep_duration():
  for guard in guards:
    print("Guard {} slept total of {}".format(guard, guards[guard]["total_asleep"]))

def decompress_sleep_duration(start, end):
  temp = []
  start = int(start)
  end = int(end)
  if end > start: 
    for i in range(start, end):
      temp.append(i)
  else:
    for i in range(start, 60):
      temp.append(i)
    for j in range(0, end):
      temp.append(j)
  return temp

def get_all_sleep_duration(guard):
  sleeps = []
  for date in guards[guard]["duty"]:
    arr = guards[guard]["duty"][date]
    for i in arr:
      temp = decompress_sleep_duration(i[0],i[1])
      sleeps.extend(temp)
  return sleeps

def get_highest_asleep_time(arr):
  return max(arr,key=arr.count)

def part2():
  counts = {}
  guard_2 = ""
  minute_2 = 0
  freq_2 = 0
  for guard in guards:
    decompressed = get_all_sleep_duration(guard)
    unique_min = set(decompressed)
    for i in unique_min: 
      if decompressed.count(i) > freq_2:
        freq_2 = decompressed.count(i)
        minute_2 = i
        guard_2 = guard 

  print('guard {} is most freq asleep at {} min'.format(guard_2, minute_2))
  print(1297*37)
# guard = {'1': 'duty':{}}
parse_file('day4.txt')
part2()
# get_total_sleep_duration()
# print(guards)
# print(get_sleep_beauty()) # 1439
# sleeps = get_all_sleep_duration("1439")
# print(sleeps)
# print(get_highest_asleep_time(sleeps))
# part1 = 1439 * 42 
# print(part1)