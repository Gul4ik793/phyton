from Node import Node, LinkedList, summ_list


def test_add(linked_list, other, expected_result):
    linked_list.add_in_tail(Node(other))
    result = [node.value for node in linked_list]
    assert result == expected_result, f"ожидал {expected_result}, но получил {result} для {linked_list}"

def test_find(linked_list, other, expected_result):
    linked_list.find(Node(other))
    result =  linked_list.find(Node(other))
    assert result.value == expected_result, f"ожидал {expected_result}, но получил {result} для {linked_list}"

def test_delete(linked_list, other, expected_result):
    linked_list.delete(Node(other))
    result = [node.value for node in linked_list]
    assert result == expected_result, f"ожидал {expected_result}, но получил {result} для {linked_list}"

def test_clean(linked_list, expected_result):
    linked_list.clean()
    result = [node.value for node in linked_list]
    assert result == expected_result, f"ожидал {expected_result}, но получил {result} для {linked_list}"

def test_len(linked_list, expected_result):
    result = linked_list.len()
    assert result == expected_result, f"ожидал {expected_result}, но получил {result} для {linked_list}"


n1 = Node(12)
n2 = Node(55)

s_list = LinkedList()
s2_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s2_list.add_in_tail(Node(11))
s2_list.add_in_tail(Node(54))

print("Положительный тест test_add")
test_add(s_list, 12, [12, 55, 12])
print()
#print("Тест с ошибкой test_add")
#test_add(s_list, 12, [12, 55, 15])
print("Положительный тест test_delete")
test_delete(s_list, 12, [12, 55, 12])
print()
#print("Тест с ошибкой test_delete")
#test_delete(s_list, 12, [12, 55, 15])
print("Положительный тест test_clean")
test_clean(s_list, [])
print()
#print("Тест с ошибкой test_clean")
#test_clean(s_list, None)
print("Положительный тест test_len")
test_len(s2_list, 2)
print()
#print("Тест с ошибкой test_len")
#test_len(s2_list, 3)










