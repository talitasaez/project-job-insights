from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    job = read(path)
    set_industries = set()
    for jobs in job:
        if jobs["industry"] != '':
            set_industries.add(jobs["industry"])

    return set_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job["industry"] == industry]
