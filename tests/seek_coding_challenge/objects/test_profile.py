import pytest
from pyspark import Row

from datetime import date
from seek_coding_challenge.objects.job import Job
from seek_coding_challenge.objects.profile import Profile


def test_profile_get_average_salary_should_handle_no_job_history():
    """Should run the test successfully."""
    profile = Profile({"firstName": "jack", "lastName": "smith", "jobHistory": []})
    result = profile.get_average_salary()
    expected = None
    assert result == expected


def test_profile_get_average_salary_should_return_average():
    """Should run the test successfully."""
    profile = Profile(
        {
            "firstName": "jack",
            "lastName": "smith",
            "jobHistory": [
                {
                    "title": "engineer",
                    "location": "melbourne",
                    "salary": 150000,
                    "fromDate": "2020-01-01",
                    "toDate": "2020-01-02",
                },
                {
                    "title": "engineer",
                    "location": "melbourne",
                    "salary": 130000,
                    "fromDate": "2020-01-03",
                    "toDate": "2020-01-04",
                },
            ],
        }
    )
    result = profile.get_average_salary()
    expected = 140000
    assert result == expected
