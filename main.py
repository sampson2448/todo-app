todos = []

while True:
    user_action = input("Type add,edit, exit or show: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
                todo = input("Enter a todo: ")
                todos.append(todo)
        case 'show' | "display":
                for index, item in enumerate(todos):
                    print(index, item)
        case 'edit':
                print(todos)
                number = int(input("number of the todo to edit: "))
                number = number - 1
                new_todo = input("enter new todo")
                todos[number] = new_todo
                print()
        case 'bye':
               break
print("bye")
