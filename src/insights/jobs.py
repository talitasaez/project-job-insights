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
        set_job.add(jobs["job_type"])
    return set_job


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job['job_type'] == job_type]
