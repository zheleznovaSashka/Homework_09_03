"""
Модуль с тестами для ExtendedLinkedList.
"""

import unittest
from double_linked_list import LinkedList, Node
from linked_list_extended import ExtendedLinkedList


class TestExtendedLinkedList(unittest.TestCase):
    """Тесты для расширенного двусвязного списка."""

    def setUp(self):
        """Подготовка перед каждым тестом."""
        self.ll = ExtendedLinkedList()

    def test_len_ll_empty(self):
        """Тест длины пустого списка."""
        self.assertEqual(self.ll.len_ll(), 0)

    def test_len_ll_with_elements(self):
        """Тест длины списка с элементами."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        self.assertEqual(self.ll.len_ll(), 3)

    def test_print_ll_from_tail(self):
        """Тест печати с хвоста."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        result = self.ll.print_ll_from_tail()
        self.assertEqual(result, [1, 2, 3])

    def test_insert_at_index_beginning(self):
        """Тест вставки в начало по индексу."""
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        result = self.ll.insert_at_index(0, 1)
        self.assertTrue(result)
        self.assertEqual(self.ll.len_ll(), 3)

    def test_insert_at_index_middle(self):
        """Тест вставки в середину по индексу."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(3)
        result = self.ll.insert_at_index(1, 2)
        self.assertTrue(result)
        self.assertEqual(self.ll.len_ll(), 3)

    def test_insert_at_index_end(self):
        """Тест вставки в конец по индексу."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        result = self.ll.insert_at_index(2, 3)
        self.assertTrue(result)
        self.assertEqual(self.ll.len_ll(), 3)

    def test_insert_at_index_invalid(self):
        """Тест вставки по неверному индексу."""
        self.ll.insert_at_head(1)
        result = self.ll.insert_at_index(5, 2)
        self.assertFalse(result)
        self.assertEqual(self.ll.len_ll(), 1)

    def test_remove_node_index_beginning(self):
        """Тест удаления с начала по индексу."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        removed = self.ll.remove_node_index(0)
        self.assertEqual(removed, 3)
        self.assertEqual(self.ll.len_ll(), 2)

    def test_remove_node_index_middle(self):
        """Тест удаления из середины по индексу."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        removed = self.ll.remove_node_index(1)
        self.assertEqual(removed, 2)
        self.assertEqual(self.ll.len_ll(), 2)

    def test_remove_node_index_end(self):
        """Тест удаления с конца по индексу."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        removed = self.ll.remove_node_index(2)
        self.assertEqual(removed, 1)
        self.assertEqual(self.ll.len_ll(), 2)

    def test_remove_node_index_invalid(self):
        """Тест удаления по неверному индексу."""
        self.ll.insert_at_head(1)
        removed = self.ll.remove_node_index(5)
        self.assertIsNone(removed)
        self.assertEqual(self.ll.len_ll(), 1)

    def test_remove_node_data_single(self):
        """Тест удаления одного узла по данным."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        result = self.ll.remove_node_data(2)
        self.assertTrue(result)
        self.assertEqual(self.ll.len_ll(), 2)

    def test_remove_node_data_not_found(self):
        """Тест удаления несуществующего узла."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        result = self.ll.remove_node_data(5)
        self.assertFalse(result)
        self.assertEqual(self.ll.len_ll(), 2)

    def test_remove_node_data_all_occurrences(self):
        """Тест удаления всех вхождений."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(3)
        result = self.ll.remove_node_data(1, remove_all=True)
        self.assertTrue(result)
        self.assertEqual(self.ll.len_ll(), 2)

    def test_contains_from_head_found(self):
        """Тест поиска с головы - элемент найден."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        found, index = self.ll.contains_from_head(2)
        self.assertTrue(found)
        self.assertEqual(index, 1)

    def test_contains_from_head_not_found(self):
        """Тест поиска с головы - элемент не найден."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        found, index = self.ll.contains_from_head(5)
        self.assertFalse(found)
        self.assertEqual(index, -1)

    def test_contains_from_tail_found(self):
        """Тест поиска с хвоста - элемент найден."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        found, index = self.ll.contains_from_tail(2)
        self.assertTrue(found)
        self.assertEqual(index, 1)

    def test_contains_from_tail_not_found(self):
        """Тест поиска с хвоста - элемент не найден."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        found, index = self.ll.contains_from_tail(5)
        self.assertFalse(found)
        self.assertEqual(index, -1)

    def test_contains_from_with_head(self):
        """Тест contains_from с поиском с головы."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        found, index = self.ll.contains_from(2, from_head=True)
        self.assertTrue(found)
        self.assertEqual(index, 1)

    def test_contains_from_with_tail(self):
        """Тест contains_from с поиском с хвоста."""
        self.ll.insert_at_head(1)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(3)
        found, index = self.ll.contains_from(2, from_head=False)
        self.assertTrue(found)
        self.assertEqual(index, 1)

    def test_complex_scenario(self):
        """Сложный сценарий: комбинация всех методов."""
        # Добавляем элементы в голову (обратный порядок)
        self.ll.insert_at_head(10)  # Список: 10
        self.ll.insert_at_head(20)  # Список: 20, 10
        self.ll.insert_at_head(30)  # Список: 30, 20, 10

        # Проверяем длину
        self.assertEqual(self.ll.len_ll(), 3)

        # Вставляем элемент в середину (позиция 1)
        self.ll.insert_at_index(1, 25)  # Список: 30, 25, 20, 10
        self.assertEqual(self.ll.len_ll(), 4)

        # Ищем элементы с головы
        found, index = self.ll.contains_from_head(25)
        self.assertTrue(found)
        self.assertEqual(index, 1)

        # Удаляем по индексу (позиция 2, значение 20)
        removed = self.ll.remove_node_index(2)  # Удаляем 20
        self.assertEqual(removed, 20)
        self.assertEqual(self.ll.len_ll(), 3)  # Список: 30, 25, 10

        # Удаляем по данным (удаляем 30 из головы)
        result = self.ll.remove_node_data(30)
        self.assertTrue(result)
        self.assertEqual(self.ll.len_ll(), 2)  # Список: 25, 10

        # Печатаем с хвоста (должно быть: 10, 25)
        result_list = self.ll.print_ll_from_tail()
        self.assertEqual(len(result_list), 2)
        self.assertEqual(result_list[0], 10)
        self.assertEqual(result_list[1], 25)


if __name__ == "__main__":
    unittest.main()