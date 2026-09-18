# NLP Assignment 3

Two parts:

- **Question 1** – `nd_recognise.py`: an ND-RECOGNIZE implementation (DFS/BFS agenda search) for the sheeptalk NFSA (`baa*!`).
- **Question 2** – `pipeline.py`: a clinical text preprocessing pipeline (tokenise → remove stopwords → lemmatise). The block diagram is in `pipeline_diagram.mmd`.

## Setup

Requires Python 3.9+.

```sh
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -c "import nltk; [nltk.download(r) for r in ['wordnet', 'averaged_perceptron_tagger_eng']]"
```

The NLTK download is only needed for Question 2.

## Run

```sh
python3 nd_recognise.py    # prints the compiled sheeptalk NFSA
python3 pipeline.py        # prints the output of each pipeline stage
```

## Test

```sh
python3 -m unittest discover -s tests
```

Add `-v` for per-test output, or run one file, e.g. `python3 -m unittest tests/test_recogniser.py`.
