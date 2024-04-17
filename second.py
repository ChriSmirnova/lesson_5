list_1 = ['Hillel', 'AQA', 'TEST']

list_as_string = ', '.join(list_1)
print("Список у вигляді стрічки:", list_as_string)

string_as_list = list_as_string.split(', ')
print("Стрічка у вигляді списку:", string_as_list)
