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


def test_profile_get_current_job_should_handle_no_job():
    """Should run the test successfully."""
    profile = Profile({"firstName": "jack", "lastName": "smith", "jobHistory": []})
    assert profile.get_current_job() is None


def test_profile_get_current_job_should_handle_no_current_job():
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
                }
            ],
        }
    )
    assert profile.get_current_job() is None


def test_profile_get_current_job_should_return_current_job():
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
                    "toDate": None,
                }
            ],
        }
    )
    result = profile.get_current_job()
    expected = Job(
        title="engineer",
        location="melbourne",
        salary=150000,
        from_date=date.fromisoformat("2020-01-01"),
        to_date=None,
    )
    assert result == expected


def test_profile_get_current_job_should_raise_if_multiple_current_jobs():
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
                    "toDate": None,
                },
                {
                    "title": "engineer",
                    "location": "melbourne",
                    "salary": 180000,
                    "fromDate": "2020-01-02",
                    "toDate": None,
                },
            ],
        }
    )
    with pytest.raises(RuntimeError):
        _ = profile.get_current_job()


def test_profile_get_current_salary_should_handle_no_jobs():
    """Should run the test successfully."""
    profile = Profile({"firstName": "jack", "lastName": "smith", "jobHistory": []})
    assert profile.get_current_salary() is None


def test_profile_get_current_salary_should_handle_no_current_job():
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
                }
            ],
        }
    )
    assert profile.get_current_salary() is None


def test_profile_get_current_salary_should_return_current_salary():
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
                    "salary": 180000,
                    "fromDate": "2020-01-01",
                    "toDate": None,
                },
            ],
        }
    )
    result = profile.get_current_salary()
    expected = 180000
    assert result == expected


def test_profile_get_current_from_date_should_handle_no_jobs():
    """Should run the test successfully."""
    profile = Profile({"firstName": "jack", "lastName": "smith", "jobHistory": []})
    assert profile.get_current_from_date() is None


def test_profile_get_current_from_date_should_handle_no_current_job():
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
                }
            ],
        }
    )
    assert profile.get_current_from_date() is None


def test_profile_get_current_from_date_should_return_current_from_date():
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
                    "salary": 180000,
                    "fromDate": "2020-01-02",
                    "toDate": None,
                },
            ],
        }
    )
    result = profile.get_current_from_date()
    expected = date.fromisoformat("2020-01-02")
    assert result == expected


def test_profile_is_currently_working_should_handle_no_jobs():
    """Should run the test successfully."""
    profile = Profile({"firstName": "jack", "lastName": "smith", "jobHistory": []})
    assert not profile.is_currently_working()


def test_profile_is_currently_working_should_handle_no_current_job():
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
                }
            ],
        }
    )
    assert not profile.is_currently_working()


def test_profile_is_currently_working_should_return_true():
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
                    "salary": 180000,
                    "fromDate": "2020-01-02",
                    "toDate": None,
                },
            ],
        }
    )
    assert profile.is_currently_working()


def test_profile_get_highest_paying_job_should_handle_no_jobs():
    """Should run the test successfully."""
    profile = Profile({"firstName": "jack", "lastName": "smith", "jobHistory": []})
    assert not profile.get_highest_paying_job()


def test_profile_get_highest_paying_job_should_return_true():
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
                    "title": "senior engineer",
                    "location": "melbourne",
                    "salary": 210000,
                    "fromDate": "2020-01-02",
                    "toDate": None,
                },
                {
                    "title": "engineer",
                    "location": "melbourne",
                    "salary": 180000,
                    "fromDate": "2020-01-02",
                    "toDate": "2020-01-03",
                },
            ],
        }
    )
    result = profile.get_highest_paying_job()
    expected = Job(
        title="senior engineer",
        location="melbourne",
        salary=210000,
        from_date=date.fromisoformat("2020-01-02"),
        to_date=None,
    )
    assert result == expected
