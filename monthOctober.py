import calendar


def out_blue(text):
    print("\033[34m {}".format(text))


out_blue("М-ц октябрь")

c = calendar.TextCalendar()
print(c.formatmonth(2021, 10))
print("------------------------------------------------")
cl = calendar.Calendar()
rez = cl.monthdayscalendar(2021, 10)
r = list(rez)
# print(rez)
# print(rez[0])

# Выводим недели м-ца по счету
count = 1
for week in rez:
    print(count, ".", "Неделя: ", week)
    count += 1

print("\n \n" + "---------------------------------------")
for num, week in enumerate(rez, 1):
    print(str(num), ".", str(week))
