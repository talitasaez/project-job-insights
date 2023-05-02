from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    job = read(path)
    max_salary = set()
    for jobs in job:
        if jobs["max_salary"].isnumeric():
            max_salary.add(int(jobs["max_salary"]))
    return max(max_salary)


def get_min_salary(path: str) -> int:
    job = read(path)
    min_salary = set()
    for jobs in job:
        if jobs["min_salary"].isnumeric():
            min_salary.add(int(jobs["min_salary"]))
    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min = int(job['min_salary'])
        max = int(job['max_salary'])
        match_salary = int(salary)
        if max < min:
            raise ValueError()
    except Exception:
        raise ValueError('Números Inválidos')
    return match_salary <= max and match_salary >= min


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
