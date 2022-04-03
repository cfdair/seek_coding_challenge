from pyspark import Row

from datetime import date
from seek_coding_challenge.objects.job import Job


def test_job_is_current_should_return_false():
    """Should run the test successfully."""
    job = Job(
        location="melbourne",
        salary=100,
        title="software engineer",
        from_date=date.fromisoformat("2019-01-01"),
        to_date=date.fromisoformat("2022-01-01"),
    )
    assert not job.is_current()


def test_job_is_current_should_return_true():
    """Should run the test successfully."""
    job = Job(
        location="melbourne",
        salary=100,
        title="software engineer",
        from_date=date.fromisoformat("2019-01-01"),
        to_date=None,
    )
    assert job.is_current()
