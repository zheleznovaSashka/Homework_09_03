"""
Модуль с расширенным классом двусвязного списка.
Наследуется от базового LinkedList и добавляет дополнительные методы.
"""

from double_linked_list import LinkedList, Node


class ExtendedLinkedList(LinkedList):
    """
    Расширенный класс двусвязного списка.

    Добавляет методы для:
    - печати в обратном порядке
    - вставки по индексу
    - удаления по индексу и по данным
    - получения длины
    - поиска элементов с начала и с конца
    """

    def __init__(self):
        """Инициализация расширенного двусвязного списка."""
        super().__init__()

    def print_ll_from_tail(self):
        """
        Печатает список в обратном порядке от хвоста к голове.

        Возвращает:
            list: Список элементов в обратном порядке
        """
        if self.tail is None:
            print("Список пуст")
            return []

        result = []
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            result.append(current_node.data)
            current_node = current_node.prev_node

        print("Список выведен с конца")
        return result

    def insert_at_index(self, index, data):
        """
        Добавляет элемент по указанному индексу.

        Аргументы:
            index: Индекс для вставки (0 - начало списка)
            data: Данные для вставки

        Возвращает:
            bool: True если вставка успешна, False если индекс вне диапазона

        Примечание:
            Если индекс равен длине списка, элемент добавляется в конец.
            Если индекс больше длины списка, вставка не происходит.
        """
        length = self.len_ll()

        # Проверка границ
        if index < 0 or index > length:
            print(f"Ошибка: индекс {index} вне диапазона [0, {length}]")
            return False

        # Вставка в начало
        if index == 0:
            self.insert_at_head(data)
            return True

        # Вставка в конец
        if index == length:
            self.insert_at_tail(data)
            return True

        # Вставка в середину
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next_node

        # Создаем новый узел
        new_node = Node(data)

        # Связываем новый узел
        new_node.prev_node = current_node.prev_node
        new_node.next_node = current_node
        current_node.prev_node.next_node = new_node
        current_node.prev_node = new_node

        print(f"Вставлен узел с данными {data} на позицию {index}")
        return True

    def remove_node_index(self, index):
        """
        Удаляет элемент по указанному индексу.

        Аргументы:
            index: Индекс элемента для удаления

        Возвращает:
            data: Данные удаленного элемента или None если индекс недействителен
        """
        length = self.len_ll()

        if length == 0:
            print("Ошибка: список пуст")
            return None

        if index < 0 or index >= length:
            print(f"Ошибка: индекс {index} вне диапазона [0, {length - 1}]")
            return None

        # Удаление с начала
        if index == 0:
            return self.remove_from_head()

        # Удаление с конца
        if index == length - 1:
            return self.remove_from_tail()

        # Удаление из середины
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next_node

        # Переподключаем ссылки
        current_node.prev_node.next_node = current_node.next_node
        current_node.next_node.prev_node = current_node.prev_node

        removed_data = current_node.data

        # Удаляем узел
        del current_node

        print(f"Удален узел с данными {removed_data} с позиции {index}")
        return removed_data

    def remove_node_data(self, data, remove_all=False):
        """
        Удаляет элемент по данным узла.

        Аргументы:
            data: Данные для поиска и удаления
            remove_all: Если True, удаляет все вхождения (по умолчанию False)

        Возвращает:
            bool: True если хотя бы один элемент удален, False если не найден
        """
        removed = False
        current_node = self.head
        nodes_to_remove = []

        # Собираем узлы для удаления
        while current_node is not None:
            if current_node.data == data:
                nodes_to_remove.append(current_node)
                if not remove_all:
                    break
            current_node = current_node.next_node

        # Удаляем собранные узлы
        for node in nodes_to_remove:
            # Если это голова
            if node.prev_node is None:
                if node.next_node is not None:
                    self.head = node.next_node
                    node.next_node.prev_node = None
                else:
                    # Единственный элемент в списке
                    self.head = None
                    self.tail = None

            # Если это хвост
            elif node.next_node is None:
                self.tail = node.prev_node
                node.prev_node.next_node = None

            # Если это середина
            else:
                node.prev_node.next_node = node.next_node
                node.next_node.prev_node = node.prev_node

            print(f"Удален узел с данными {node.data}")
            del node
            removed = True

        if removed:
            print(f"Удаление завершено. Удалено {len(nodes_to_remove)} узлов.")
        else:
            print(f"Узел с данными {data} не найден")

        return removed

    def len_ll(self):
        """
        Возвращает длину связанного списка.

        Возвращает:
            int: Количество элементов в списке
        """
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next_node
        return count

    def contains_from_head(self, data):
        """
        Проверяет наличие элемента, начиная поиск с головы.

        Аргументы:
            data: Данные для поиска

        Возвращает:
            tuple: (bool, int) - найдено ли и индекс элемента
        """
        current_node = self.head
        index = 0

        while current_node is not None:
            if current_node.data == data:
                print(f"Элемент {data} найден на позиции {index} (поиск с головы)")
                return (True, index)
            current_node = current_node.next_node
            index += 1

        print(f"Элемент {data} не найден (поиск с головы)")
        return (False, -1)

    def contains_from_tail(self, data):
        """
        Проверяет наличие элемента, начиная поиск с хвоста.

        Аргументы:
            data: Данные для поиска

        Возвращает:
            tuple: (bool, int) - найдено ли и индекс с конца
        """
        current_node = self.tail
        index_from_tail = 0

        while current_node is not None:
            if current_node.data == data:
                print(f"Элемент {data} найден на расстоянии {index_from_tail} от хвоста (поиск с хвоста)")
                return (True, index_from_tail)
            current_node = current_node.prev_node
            index_from_tail += 1

        print(f"Элемент {data} не найден (поиск с хвоста)")
        return (False, -1)

    def contains_from(self, data, from_head=True):
        """
        Проверяет наличие элемента с выбором направления поиска.

        Аргументы:
            data: Данные для поиска
            from_head: Если True - поиск с головы, если False - с хвоста

        Возвращает:
            tuple: (bool, int) - найдено ли и индекс (с начала или с конца)
        """
        if from_head:
            return self.contains_from_head(data)
        else:
            return self.contains_from_tail(data)