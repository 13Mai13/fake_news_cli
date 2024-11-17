import pandas as pd
from unittest import mock
from lib.data_processing.extract_metadata_handler import (
    transform_news_content,
    save_metadata,
    get_metadata,
    extract_metadata,
)


def test_transform_news_content():
    sample_news = {"headline": "Test headline", "content": "Test content"}
    df = transform_news_content(sample_news)
    assert isinstance(df, pd.DataFrame)
    assert "headline" in df.columns


@mock.patch("lib.data_processing.extract_metadata.pd.DataFrame.to_csv")
def test_save_metadata(mock_to_csv):
    df = pd.DataFrame({"test": [1, 2, 3]})
    save_metadata(df, "test", "/fake/path")
    # Adjusted to account for index=False in the function call
    mock_to_csv.assert_called_once_with(
        "/fake/path/metadata_test_processed.csv", index=False
    )


@mock.patch("lib.data_processing.extract_metadata.os.listdir")
@mock.patch(
    "lib.data_processing.extract_metadata.open",
    new_callable=mock.mock_open,
    read_data='{"headline": "fake headline"}',
)
def test_get_metadata(mock_open, mock_listdir):
    # Mocking listdir to return two JSON files
    mock_listdir.return_value = ["file1.json", "file2.json"]
    content_types = ["RealNewsContent", "FakeNewsContent"]
    root_path = "/fake/root"
    dataset_name = "FakeDataset"

    # Call function
    df = get_metadata(dataset_name, root_path, content_types)

    # Assertions
    assert isinstance(df, pd.DataFrame)
    assert "is_fake" in df.columns
    # Adjusted to 4 since each file will be read twice with different content_types
    assert len(df) == 4


@mock.patch("lib.data_processing.extract_metadata.save_metadata")
@mock.patch("lib.data_processing.extract_metadata.get_metadata")
def test_extract_metadata(mock_get_metadata, mock_save_metadata):
    # Mocking return values for get_metadata
    mock_get_metadata.return_value = pd.DataFrame({"col": [1, 2, 3]})

    # Run the function with test arguments
    extract_metadata(
        datasets=["TestDataset"],
        root_path="/fake/root",
        content_types=["RealNewsContent"],
        path="/fake/path",
    )

    # Check that get_metadata was called with expected arguments
    mock_get_metadata.assert_called_once_with(
        dataset_name="TestDataset",
        root_path="/fake/root",
        content_types=["RealNewsContent"],
    )

    # Ensure save_metadata is called, avoiding actual file write
    mock_save_metadata.assert_called_once()
