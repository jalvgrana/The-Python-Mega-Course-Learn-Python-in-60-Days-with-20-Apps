todos = ['clean', 'add', 'show']

print("Primera forma sin indices")
for items in todos:
    print(items)

print("\nSegunda forma con indices")
for item in enumerate(todos):
    print(item)

print("\nTercera forma con indices")
for index, item in enumerate(todos):
    print(index, item)