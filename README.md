# Wordle Solver

## Introduction
This project contains a Python-based Wordle solver. The solver uses a list of words extracted from a specific URL using `word_extractor.py`. This script is tailored to extract words only from the designated URL.

## Prerequisites
- Python 3.x
- Dependencies as listed in `requirements.txt` (if any)

## Setup
1. Clone the repository or download the source code.
2. Install necessary Python dependencies (if any are listed in `requirements.txt`).

## Word Extraction
To extract more words, run the following command:

```bash
python word_extractor.py
```

### Usage
- Choose the length of the word you are interested in.
- Copy the URL from the website where the words are listed.
- Open `word_extractor.py` and paste the URL into the `url` variable.
- Run the script. Extracted words will be saved in `words.txt`.

## Running the Wordle Solver
To use the Wordle solver, execute:

```bash
python wordle_solver.py
```

### How to Use
- When prompted for your guess, enter the word you submitted on the Wordle site.
- For the result, enter the colors corresponding to each letter:
  - `g` for green (correct letter, correct position)
  - `y` for yellow (correct letter, wrong position)
  - `_` (underscore) for grey (letter not in the word)
- If multiple words match the criteria, the solver will continue to narrow down the possibilities.

## Contribution
Feel free to contribute to this project by submitting pull requests or suggesting improvements.
