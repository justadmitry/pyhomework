#task 1
HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks)
  elif command == "add":
    task = input("Введите название задачи: ")
    tasks.append(task)
    print("Задача добавлена")
  elif command == "exit":
    print("Спасибо за использование!")
    break
  else: 
    print("Неизвестная команда")
    break

print("До свидания!")



#task 2

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = []
today = []
tommorow = []
other = []
run = True

while run:
  command = input("Введите команду: ")

  if command == "help":
    print(HELP)

    
  elif command == "show":
    print(today)
    print(tommorow)
    print(other)
    
  elif command == "add":
    date = input("Введите дату: ")
    if date == "Сегодня":
      today.append(input("Введите задачу: "))
    if date == "Завтра":
      tommorow.append(input("Введите название задачи: "))
    else:
      other.append(input("Введите название задачи: "))
    print("Задача добавлена")

  elif command == "exit":
    print("Спасибо за использование!")
    break

  else: 
    print("Неизвестная команда")
    break

print("До свидания!")
