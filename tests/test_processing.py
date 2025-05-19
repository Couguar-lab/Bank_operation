from src.processing import filter_by_state, sort_by_date
from tests.conftest import sort_state_executed_answer


def test_filter_by_state(coll_sort, sort_state_executed_answer):
    filter_by_state(coll_sort) == sort_state_executed_answer


def test_sort_by_date(coll_sort, sort_data_answer):
    sort_by_date(coll_sort) == sort_data_answer
