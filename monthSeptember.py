import calendar
# import rich
import color
from rich.console import Console
from rich import print

console = Console()
console.rule("[bold red]Part 1")

blue_console = Console(style="white on blue")
blue_console.print("I'm blue. Da ba dee da ba di.")

console = Console(width=20)

style = "bold white on blue"
console.print("Rich", style=style)
console.print("Rich", style=style, justify="left")
console.print("Rich", style=style, justify="center")
console.print("Rich", style=style, justify="right")

console.print("Привет, [bold magenta]мир![/bold magenta] :smile:")

c = calendar.TextCalendar()
# print(c)
print(c.formatmonth(2021, 9))
cl = calendar.Calendar()
rez = cl.monthdayscalendar(2021, 9)

for num, week in enumerate(rez, 1):
    print(str(num), "Неделя", ".", str(week))

print(
    "\n \n" + "---------------------------------------*************************************************************************")

rez = cl.monthdayscalendar(2021, 9)
print(rez)
print(rez[0])

nameDayWeek = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
oneWeek = dict(zip(nameDayWeek, rez[0]))
print(oneWeek)

dictMonthSeptember = dict()

for i in range(0, 5):
    oneWeek[i] = dict(zip(rez[i], nameDayWeek))
    dictMonthSeptember.update(oneWeek[i])
    i += 1
# print(dictMonthSeptember)
# print(dictMonthSeptember.items())

# for key, value in dictMonthSeptember.items():
#     print(key, value)




# print(str(week[1]))

# v = c.prmonth(2021, 9)
