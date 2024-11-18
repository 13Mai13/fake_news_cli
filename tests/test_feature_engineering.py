"""
All the test realted to the feature_engineering.py
"""

import pytest
import pandas as pd
from lib.feature_engineering.feature_engineering import shuffle_data


@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": ["a", "b", "c", "d", "e"]})


def test_shuffle_data_preserves_data(sample_dataframe):
    shuffled_df = shuffle_data(sample_dataframe)
    pd.testing.assert_frame_equal(
        shuffled_df.sort_index(axis=0),
        sample_dataframe.sort_index(axis=0),
        check_like=True,
    )


def test_shuffle_data_randomizes_order(sample_dataframe):
    shuffled_df = shuffle_data(sample_dataframe)
    assert not sample_dataframe.equals(
        shuffled_df
    ), "Dataframe order was not randomized"


def test_shuffle_data_preserves_length(sample_dataframe):
    shuffled_df = shuffle_data(sample_dataframe)
    assert len(shuffled_df) == len(sample_dataframe)
