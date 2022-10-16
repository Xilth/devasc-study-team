import unittest

from recursive_json_search import *
from test_data import *

class json_search_test(unittest.TestCase):
    def test_search_found(self):
        self.assertTrue([]!=json_search(key1,data))
    def test_search_not_found(self):
        self.assertTrue([]==json_search(key2,data))
    def test_is_a_list(self):
        self.assertIsInstance(json_search(key1,data),list)
    ret_val = []
    def json_search(key, input_object):
        if isinstance(input_object, dict):
            for k, v in input_object.items():
                if k == key:
                    temp = {k:v}
                    ret_val.append(temp)
    def __main__():
        if __name__ == '__main__':
            unittest.main()
