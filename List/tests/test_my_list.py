import unittest

from my_list import MyList


class TestMyList(unittest.TestCase):
    def test_is_empty_true(self):
        new_list = MyList()
        self.assertTrue(new_list.empty())

    def test_is_empty_false(self):
        new_list = MyList()
        new_list.add("test1")
        self.assertFalse(new_list.empty())

    def test_add_items(self):
        new_list = MyList()
        new_list.add(1)
        new_list.add(2)
        new_list.add(3)
        self.assertEqual(new_list[2], 3)
        self.assertNotEqual(new_list[0], None)

    def test_set_item(self):
        new_list = MyList()
        new_list.add(1)
        new_list.add(2)
        new_list.add(3)
        new_list[1] = 5
        self.assertEqual(new_list[1], 5)

    def test_list_len_3(self):
        new_list = MyList()
        new_list.add(1)
        new_list.add(2)
        new_list.add(3)
        self.assertEqual(len(new_list), 3)

    def test_contains_item_true(self):
        new_list = MyList()
        new_list.add(1)
        new_list.add(2)
        new_list.add(3)
        self.assertIn(2, new_list)

    def test_contains_item_false(self):
        new_list = MyList()
        new_list.add(1)
        new_list.add(2)
        new_list.add(3)
        self.assertNotIn(4, new_list)

    def test_print_list_3_items(self):
        new_list = MyList()
        new_list.add(1)
        new_list.add(2)
        new_list.add(3)
        self.assertEqual(str(new_list), "[1,2,3]")

    def test_print_list_empty(self):
        new_list = MyList()
        self.assertEqual(str(new_list), "[]")



