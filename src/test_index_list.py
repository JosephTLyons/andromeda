import pytest

from index_list import IndexList


class TestIndexList():
    def test_base_rollovers(self):
        length = 5
        bases = [10, 26, 62, 94]

        for base in bases:
            index_list = IndexList(length, base)

            for i in range(length):
                index_list.increaseBy(base ** i)

            new_list = []

            for i in range(index_list.len()):
                new_list.append(index_list.at(i))

            assert [1, 1, 1, 1, 1] == new_list
