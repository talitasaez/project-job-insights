from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        content = csv.DictReader(file)
        job_list = []
        for job in content:
            job_list.append(job)
    return job_list


def get_unique_job_types(path: str) -> List[str]:
    job = read(path)
    set_job = set()
    for jobs in job:
        set_job.add(jobs['job_type'])
    return set_job


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
