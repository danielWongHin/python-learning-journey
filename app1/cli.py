from functions import get_todos, write_todos
# import fucntions; functions.get_todo()
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:

    user_action = input("Type add, edit, complete, show or exit: ")

    # 9. We can use the strip()_ method to remove the space of the string
    user_action = user_action.strip()

    if user_action.startswith("add"):
        if user_action != "add":
            todo = user_action[4:]
        else:
            todo = input("Enter the todo: ")

        # file = open("files/todos.txt", "r")
        # todos = file.readlines()
        # file.close()
        # You don't need to close the file with with-context-manager

        todos = get_todos()

        todos.append(todo + "\n")

        # file = open('files/todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        write_todos(todos)
        # 11. We can use | as the OR operator

    elif user_action.startswith("show"):
        # 8. We can use the for loop to read the String; the for loop will go through all the sequence of the
        # object, eg, string, list
        # file = open("files/todos.txt", "r")
        # todos = file.readlines()
        # file.close()
        todos = get_todos()
        # new_todos = []
        # List comprehension
        # for item in todos:
        #     new_item = item.strip("\n")
        #     new_todos.append(new_item)
        # new_todos = [item.strip("\n") for item in todos]
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")

    elif user_action.startswith("exit"):
        break
    # 10. If the case isn't match any of yours, you can use _ to do the operation

    elif user_action.startswith("edit"):
        try:

            if user_action == "edit":
                number = int(input("Number of the todo to edit: "))
            else:
                number = int(user_action[5:])

            number = number - 1
            todos = get_todos()
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            if user_action != "complete":
                number = int(user_action[9:])
            else:
                number = int(input("Number of the todo to complete: "))
            todos = get_todos()
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)
            write_todos(todos)
            message = f"Todo {todo_to_remove} has been remove from the list"
            print(message)

        except IndexError:
            print("There is no item with that number")
    else:
        print("You are entered an unknown command")
print("Bye!")
