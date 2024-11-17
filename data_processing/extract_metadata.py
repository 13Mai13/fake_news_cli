"""
This are all the commands about data processing
"""

import json
import os

import pandas as pd
from typing import Dict, Any

DATASETS = ["BuzzFeed", "PolitiFact"]
ROOT_PATH = "/Users/mai/code-stuff/FakeNewsNet/Data/"
TYPES = ["RealNewsContent", "FakeNewsContent"]


def transform_news_content(new: Dict) -> pd.DataFrame:
    return pd.DataFrame.from_dict(new, orient="index").T


def get_metadata(dataset_name: str, path: str):
    # TODO: Error handling
    news = pd.DataFrame()
    news_type = []
    for content_type in TYPES:
        relative_path = f"{ROOT_PATH}/{dataset_name}/{content_type}"
        for file_name in os.listdir(relative_path):
            with open(f"{relative_path}/{file_name}", "r") as file:
                new = json.load(file)
                new = transform_news_content(new)
            news = pd.concat([news, new], ignore_index=True)
            if content_type == "RealNewsContent":
                news_type.append(False)
            else:
                news_type.append(True)
    news["is_fake"] = news_type
    if path:
        pass
    else:
        news.to_csv(f"metadata_{dataset_name}_processed.csv")


def extract_metadata(file: str) -> Dict[str | Any]:
    """
    # TODO: Handle multiple options (pass one dataset, extract all)
    """
    for dataset in DATASETS:
        get_metadata(
            dataset=dataset,
        )
