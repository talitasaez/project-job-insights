from src.pre_built.counter import count_ocurrences


def test_counter():
    counter_all = count_ocurrences(('data/jobs.csv'), 'python')
    assert counter_all == 1639
