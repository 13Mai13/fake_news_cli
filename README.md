# fake_news_cli

This is the CLI that makes possible my PhD research

## Setup

Python 3.12

### Install pre-commit

1. Run `pre-commit install`
2. Run `pre-commit run --all-files` -> check all the files are correct

### MyPy

- Run mypy across all files `python -m mypy . ` 

# Extract data

You need to have [FakeNewsNet](https://github.com/KaiDMML/FakeNewsNet) downloaded in the same level: 

```
.
├── FakeNewsNet
...
├── fake_news_cli
```