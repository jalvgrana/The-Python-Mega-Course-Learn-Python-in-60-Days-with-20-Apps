user_prompt = "Enter a todo (min dos palabras...): "
todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo.title())
    print(todos)