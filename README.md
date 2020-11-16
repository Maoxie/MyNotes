# MyNotes

Based on MkDocs to build markdown files as docs pages.

## 1. Requirements

Python
MkDocs
pymdown-extensions==8.0.1

## 2. Install

```bash
python -m pip install -r requirements.txt

# clone the notes repository and rename it as docs
git clone git@github.com/xxxxxx/Notes.git
mv Notes docs
```

```bash
# serve
python -m mkdocs serve
# or build
# python -m mkdocs build
```
