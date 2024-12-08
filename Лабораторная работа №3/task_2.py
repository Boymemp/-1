# TODO Напишите функцию find_common_participants
def find_common_participants(list1, list2, delimeter = ','):
    list1 = list1.split(delimeter)
    list2 = list2.split(delimeter)
    common_participants = list(set(list1).intersection(list2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, delimeter = '|')
print(result)

# TODO Провеьте работу функции с разделителем отличным от запятой
