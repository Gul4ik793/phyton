from Node import Node, LinkedList, summ_list



n1 = Node(12)
n2 = Node(55)

s_list = LinkedList()
s2_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s2_list.add_in_tail(Node(11))
s2_list.add_in_tail(Node(54))



print(f"Результат п. 1.8 - сложение одинаковых списков: {summ_list(s_list, s2_list)}")
print()
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(128))
print(f"Результат п. 1.8 - сложение разных по длине списков: {summ_list(s_list, s2_list)}")
print()

length = s_list.len()
print(f"Результат 1.5 - длина списка: {length} элемента(ов)")
print()

sp1 = s_list.find(12)
print(f"Результат п. 1.4 - найденный узел (только первый): {sp1}")
sp = s_list.find_all(128)
print(f"Результат п. 1.4 - питоновский список всех найденных узлов: {sp}")
print()

sp = s_list.find_all_list()
print(f"Вывод узлов в виде списка: {sp}")
print()

print("Поэлементный вывод связанного списка:")
s_list.print_all_nodes()
print()


print("Результат п. 1.1 - удаление элемента '12'-первый нашедший элемент:")
s_list.delete(12)
s_list.print_all_nodes()
print()

print("Результат п. 1.6 - добавление элемента '12'-после элемента '55':")
s_list.insert(55, Node(12))
s_list.print_all_nodes()
print()

print("Результат п. 1.6 - добавление элемента '12'-после элемента '55' еще раз:")
s_list.insert(55, Node(12))
s_list.print_all_nodes()
print()

print("Результат п. 1.2 - удаление элемента '12'-все нашедшие элемент в списке:")
s_list.delete(12, True)
s_list.print_all_nodes()
print()

print("Результат п. 1.3 -очистила список:")
s_list.clean()
s_list.print_all_nodes()
print()

print("Результат п. 1.2 - удаление элемента '128' в пустом списке- вывод ошибки:")
s_list.delete(128)
s_list.print_all_nodes()

