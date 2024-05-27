waiting_list = ['sen', 'ben', 'john']
waiting_list.sort()
'''
no hace falta waiting_list = waiting_list.sort()
porque las listas son iterables y mutables
'''

for index, item in enumerate(waiting_list):
    row = f'{index +1}.{item.capitalize()}'
    print(row)


print('Hello'.replace('o', 'x'))

waiting_list = ['sen', 'ben', 'john']
waiting_list.sort(reverse=True)

for index, item in enumerate(waiting_list):
    row = f'{index +1}.{item.capitalize()}'
    print(row)


