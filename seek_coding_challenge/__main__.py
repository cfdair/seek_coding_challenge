#!/usr/bin/env python
# encoding: utf-8
"""Print and answer all questions."""

import logging
from typing import Callable, Any, List

from pyspark.sql import DataFrame, SparkSession
from pyspark import SparkConf
from pyspark.sql import functions as f


def main(args: List[str]) -> None:
    """Execute the main function.

    This will answer all of the questions posed.
    """
    print("Beginning process...")
    spark = get_local_spark_session()
    df = question_1(spark)
    # question_2(df)
    # question_3(df)
    question_4(df)
    question_5(df)
    question_6(df)
    question_7(df)
    question_8(df)
    question_9(df)
    question_10(df)
    question_11(df)
    question_12(df)


def question_1(spark: SparkSession) -> DataFrame:
    """Print question 1 and provide the answer."""
    print("Q1. Please load the dataset into a Spark dataframe. "
    "You may want to look at the data first using jq or a similar tool "
    "to get an idea of how the data is structured.")
    fail
    print("Question 1 complete.")
    return df


def question_2(df: DataFrame) -> None:
    """Print question 2 and provide the answer."""
    print("Q2. Print the schema.")
    fail
    print("Question 2 complete.")


def question_3(df: DataFrame) -> None:
    """Print question 3 and provide the answer."""
    print("Q3. How many records are there in the dataset?")
    fail
    print("Question 3 complete.")


def question_4(df: DataFrame) -> None:
    """Print question 4 and provide the answer."""
    print("Q4. What is the average salary for each "
                "profile? Display the first 10 results, "
                "ordered by lastName in descending order.")
    fail
    print("Question 4 complete.")


def question_5(df: DataFrame) -> None:
    """Print question 5 and provide the answer."""
    print("Q5. What is the average salary across the whole dataset?")
    fail
    print("Question 5 complete.")


def question_6(df: DataFrame) -> None:
    """Print question 6 and provide the answer."""
    print("Q6. On average, what are the top 5 paying jobs? "
                "Bottom 5 paying jobs? If there is a tie, please "
                "order by title, location.")
    fail
    print("Question 6 complete.")


def question_7(df: DataFrame) -> None:
    """Print question 7 and provide the answer."""
    print("Q7. Who is currently making the most money? "
                "If there is a tie, please order in "
                "lastName descending, fromDate descending.")
    fail
    print("Question 7 complete.")


def question_8(df: DataFrame) -> None:
    """Print question 8 and provide the answer."""
    print("Q8. What was the most popular job title started in 2019?")
    fail
    print("Question 8 complete.")


def question_9(df: DataFrame) -> None:
    """Print question 9 and provide the answer."""
    print("Q9. How many people are currently working?")
    fail
    print("Question 9 complete.")


def question_10(df: DataFrame) -> None:
    """Print question 10 and provide the answer."""
    print("Q10. For each person, list only their latest job. "
                "Display the first 10 results, ordered by "
                "lastName descending, firstName ascending order.")
    fail
    print("Question 10 complete.")


def question_11(df: DataFrame) -> None:
    """Print question 11 and provide the answer."""
    print("Q11. For each person, list their highest "
                "paying job along with their first name, "
                "last name, salary and the year they made "
                "this salary. Store the results in a dataframe, "
                "and then print out 10 results.")
    fail
    print("Question 11 complete.")


def question_12(df: DataFrame) -> None:
    """Print question 12 and provide the answer."""
    print("Q12. Write out the last result (question 11) in parquet format, compressed, partitioned by year of their highest paying job.")
    fail
    print("Question 12 complete.")


def get_local_spark_session() -> SparkSession:
    """Create the local spark session.

    Returns:
        SparkSession: The loaded spark session.
    """
    print("Initialising spark...")
    spark_conf = SparkConf().setMaster("local[2]").setAppName("local-testing")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    return spark


if __name__ == "__main__":
    ARGS = []
    main(ARGS)
