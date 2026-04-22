# ExtendedLinkedList - Расширенный двусвязный список

## Описание
Класс-наследник от `LinkedList`, реализующий дополнительные методы для работы с двусвязным списком.

## Методы

### Основные методы
- `print_ll_from_tail()` - печать списка от хвоста к голове
- `insert_at_index(index, data)` - вставка элемента по индексу
- `remove_node_index(index)` - удаление элемента по индексу
- `remove_node_data(data, remove_all=False)` - удаление элемента по данным
- `len_ll()` - получение длины списка
- `contains_from_head(data)` - поиск с головы
- `contains_from_tail(data)` - поиск с хвоста
- `contains_from(data, from_head=True)` - поиск с выбором направления

## Запуск тестов

```bash
# Все тесты
python -m unittest test_extended_linked_list.py -v

# Coverage
coverage run -m unittest test_extended_linked_list.py
coverage report -m
coverage html