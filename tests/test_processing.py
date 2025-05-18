from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(coll_sort, sort_state_executed_test):
    filter_by_state(coll_sort) == sort_state_executed_test


def test_sort_by_date(coll_sort, sort_data_test):
    sort_by_date(coll_sort) == sort_data_test
