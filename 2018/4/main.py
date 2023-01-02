from datetime import datetime, timedelta

input = open(0).read().strip().splitlines()

ordered = []

for x in input:
    time, data = x.split("] ")
    ordered.append((time[1:], data))

ordered.sort(key=lambda date: datetime.strptime(date[0], "%Y-%m-%d %H:%M"))

guards = {}

current_guard = ""
fell_asleep = ""
woke_up = ""

for item in ordered:
    date, time = item[0].split()
    data = item[1].split()

    # Y = date.split("-")[0]
    # m = date.split("-")[1]
    # d = date.split("-")[1]
    # H = time.split(":")[0]
    # M = time.split(":")[1]

    if len(data) == 4:
        current_guard = data[1][1:]
    if data[0] == "falls":
        fell_asleep = time
    if data[0] == "wakes":
        woke_up = time
        if current_guard in guards:
            guards[current_guard].append((fell_asleep, woke_up))
        else:
            guards[current_guard] = [(fell_asleep, woke_up)]

totals = {}

for guard in guards:
    totals[guard] = 0
    cycles = guards[guard]
    for cycle in cycles:
        start = list(map(int, cycle[0].split(":")))
        end = list(map(int, cycle[1].split(":")))
        sleeping = str(
            timedelta(hours=end[0], minutes=end[1])
            - timedelta(hours=start[0], minutes=start[1])
        )

        ll = list(map(int, sleeping.split(":")))
        hours, mins = ll[0], ll[1]

        totals[guard] += hours * 60 + mins


most = 0
sleeper = ""
for guard in totals:
    if totals[guard] > most:
        most = totals[guard]
        sleeper = guard

sleep_times = guards[sleeper]

all_minutes = {}

for guard in guards:
    all_minutes[guard] = {}
    for time in guards[guard]:
        for x in range(int(time[0][3:]), int(time[1][3:])):
            if x in all_minutes[guard]:
                all_minutes[guard][x] += 1
            else:
                all_minutes[guard][x] = 1

print(all_minutes)


minutes = {}

for time in sleep_times:
    for x in range(int(time[0][3:]), int(time[1][3:])):
        X = f"00:{x}"
        if X in minutes:
            minutes[X] += 1
        else:
            minutes[X] = 1

most_slept = 0
most = ""

for item in minutes:
    if int(minutes[item]) > most_slept:
        most_slept = int(minutes[item])
        most = item


most_slpt = 0
most_guard = ""
for guard in all_minutes:
    for minute in all_minutes[guard]:
        if all_minutes[guard][minute] > most_slpt:
            most_slpt = minute
            most_guard = guard

print(int(most_guard) * most_slpt)

# print(most)

# print(int(sleeper) * int(most[3:]))
