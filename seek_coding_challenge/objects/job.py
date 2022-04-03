#!/usr/bin/env python
# encoding: utf-8
"""The job class representing a job a profile has/had."""

from dataclasses import dataclass
from datetime import date
from typing import Optional
from pyspark.sql import types as t

JOB_PYSPARK_STRUCT = (
    t.StructType()
    .add("location", t.StringType())
    .add("salary", t.IntegerType())
    .add("title", t.StringType())
    .add("from_date", t.DateType())
    .add("to_date", t.DateType())
)

@dataclass
class Job:
    """The job that a profile has/had."""

    location: str
    salary: int
    title: str
    from_date: date
    to_date: Optional[date]

    def is_current(self) -> bool:
        """Whether this job currently being worked.

        Returns:
            bool: Whether this job currently being worked.
        """
        return self.to_date is None

