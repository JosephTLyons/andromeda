import pytest

from src.index_list import IndexList


class TestIndexList:
    def test_base_rollover_increase_by_1(self):
        length = 2
        base = 2

        index_list = IndexList(length, base)
        number_of_increases = (base ** length) - 1

        for _ in range(number_of_increases):
            index_list.increase_by(1)

        assert [1, 1] == index_list.index_list

    def test_base_rollover_with_even_overflow(self):
        length = 2
        base = 2

        index_list = IndexList(length, base)

        assert not index_list.has_overflowed

        number_of_increases = base ** length

        for _ in range(number_of_increases):
            index_list.increase_by(1)

        assert [0, 0] == index_list.index_list
        assert index_list.has_overflowed

    def test_base_rollover_with_overflow_plus_remainder(self):
        length = 2
        base = 2

        index_list = IndexList(length, base)

        assert not index_list.has_overflowed

        index_list.increase_by(5)

        assert [0, 1] == index_list.index_list
        assert index_list.has_overflowed

    def test_with_various_bases(self):
        length = 5
        bases = [10, 26, 62, 94]

        for base in bases:
            index_list = IndexList(length, base)

            for i in range(length):
                index_list.increase_by(base ** i)

            assert [1, 1, 1, 1, 1] == index_list.index_list

    def test_base_rollover_increase_by_larger_than_base(self):
        length = 3
        base = 10

        index_list = IndexList(length, base)
        index_list.increase_by(20)

        assert [0, 2, 0] == index_list.index_list

    def test_init(self):
        index_list = IndexList(5, 10)
        assert [0, 0, 0, 0, 0] == index_list.index_list
        assert len(index_list) == 5
        assert not index_list.has_overflowed

    def test_length(self):
        assert len(IndexList(5, 10)) == 5

    def test_increment_by_neg_error(self):
        with pytest.raises(ValueError):
            IndexList(5, 2).increase_by(-1)

    def test_get_index_string(self):
        index_list = IndexList(5, 10)
        assert "00 00 00 00 00 " == index_list.get_index_string()
        index_list.increase_by(15214)
        assert "01 05 02 01 04 " == index_list.get_index_string()

    def test_large_increment(self):
        index_list = IndexList(5, 12)
        index_list.increase_by(92392)
        assert [4, 5, 5, 7, 4] == index_list.index_list
