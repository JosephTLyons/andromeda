import pytest

from index_list import IndexList


class TestIndexList():
    def test_base_rollover_increase_by_1(self):
        length = 2
        base = 2

        index_list = IndexList(length, base)

        for i in range((base ** length) - 1):
            index_list.increaseBy(1)

        new_list = []

        for i in range(index_list.len()):
            new_list.append(index_list.at(i))

        assert [1, 1] == new_list

    def test_base_rollover_reset_to_zero(self):
        length = 2
        base = 2

        index_list = IndexList(length, base)

        assert index_list.hasResetToZero == False

        for i in range(base ** length):
            index_list.increaseBy(1)

        new_list = []

        for i in range(index_list.len()):
            new_list.append(index_list.at(i))

        assert [0, 0] == new_list
        assert index_list.hasResetToZero == True

    def test_base_rollover_reset_to_zero_with_remainder(self):
        length = 2
        base = 2

        index_list = IndexList(length, base)

        assert index_list.hasResetToZero == False

        index_list.increaseBy(5)

        new_list = []

        for i in range(index_list.len()):
            new_list.append(index_list.at(i))

        assert [0, 1] == new_list
        assert index_list.hasResetToZero == True

    def test_base_rollover_increase_by_larger_than_base(self):
        length = 3
        base = 10

        index_list = IndexList(length, base)
        index_list.increaseBy(20)

        new_list = []

        for i in range(index_list.len()):
            new_list.append(index_list.at(i))

        assert [0, 2, 0] == new_list

    def test_length(self):
        index_list = IndexList(5, 10)
        assert 5 == index_list.len()

    def test_increment_by_neg_error(self):
        index_list = IndexList(5, 2)

        with pytest.raises(ValueError):
            index_list.increaseBy(-1)