#!/usr/bin/env python
# encoding: utf-8
"""The profile class."""

from dataclasses import dataclass
from datetime import date
from typing import List, Union, Optional

from pyspark import Row

from seek_coding_challenge.objects.job import Job


@dataclass
class Profile:
    """The profile class."""

    first_name: str
    last_name: str
    job_history: List[Job]

    def __init__(self, input_data: Union[dict, Row]):
        """Initialise the Profile class.

        Args:
            input_data (Union[dict, Row]): The input data
                for this Profile.
        """
        if isinstance(input_data, Row):
            data = input_data.asDict(recursive=True)
        else:
            data = input_data
        self.first_name = data["firstName"]
        self.last_name = data["lastName"]
        job_history = []
        for job_data in data["jobHistory"]:
            if job_data["toDate"]:
                to_date = date.fromisoformat(job_data["toDate"])
            else:
                to_date = None
            job = Job(
                location=job_data["location"],
                salary=job_data["salary"],
                title=job_data["title"],
                from_date=date.fromisoformat(job_data["fromDate"]),
                to_date=to_date,
            )
            job_history.append(job)
        self.job_history = job_history

    def get_average_salary(self) -> Optional[float]:
        """Calculate the average salary of this Profile.

        None is returned if there is no job history.

        Returns:
            Optional[float]: The average salary.
        """
        if not self.job_history:
            return None

        number_of_jobs = len(self.job_history)
        average_salary = sum(x.salary for x in self.job_history) / number_of_jobs
        return round(average_salary, 2)
