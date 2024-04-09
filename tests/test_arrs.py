from utils import arrs


def test_get():
    test_list = [1, 2, 3]
    assert arrs.get(test_list, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(test_list, -2) is None
    assert arrs.get(test_list, len(test_list), "test") == "test"


def test_slice():
    test_list = [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(test_list, 1) == [2, 3]
    assert arrs.my_slice(test_list) == test_list
    assert arrs.my_slice(test_list, 0, 0) == []
    assert arrs.my_slice(test_list, 1, len(test_list) + 1) == [2, 3]
    assert arrs.my_slice([], 3, 6) == []
