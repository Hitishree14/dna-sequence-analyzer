
# DNA Sequence Analyzer

A beginner-friendly Python project for analyzing DNA sequences. This project combines basic programming with fundamental concepts in molecular biology and bioinformatics.

## Project Overview

DNA sequences contain four nitrogenous bases: adenine (A), thymine (T), guanine (G) and cytosine (C). Analyzing these sequences helps us understand nucleotide composition and other sequence properties.

This program accepts a DNA sequence and calculates its basic characteristics.

## Features

- Validates DNA sequences
- Accepts lowercase and uppercase input
- Ignores whitespace within the sequence
- Calculates sequence length
- Counts A, T, G and C nucleotides
- Calculates GC content as a percentage
- Converts the coding-strand sequence from DNA to an RNA-like sequence by replacing T with U
- Calculates the reverse complement
- Handles invalid and empty input
- Includes automated tests using Python's `unittest` module

## Technologies Used

- Python
- Git and GitHub
- Python `unittest` for testing

## How to Run

### Requirements

- Python 3 installed on your computer

### Steps

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the program:

```bash
python dna_analyzer.py
```

4. Enter a DNA sequence when prompted.

## Example

### Input

```text
ATGCGTAA
```

### Output

```text
--- DNA Sequence Analysis ---
DNA sequence: ATGCGTAA
Sequence length: 8
A count: 3
T count: 2
G count: 2
C count: 1
GC content: 37.50%
RNA sequence: AUGCGUAA
Reverse complement: TTACGCAT
```

## Biological Concepts

### 1. Nucleotide Composition

DNA contains four nitrogenous bases: adenine (A), thymine (T), guanine (G) and cytosine (C). This program counts each base in a DNA sequence.

### 2. GC Content

GC content is the percentage of nucleotides in a DNA sequence that are guanine or cytosine.

**Formula:**

GC content (%) = [(G + C) / Total sequence length] × 100

GC content is useful in sequence characterization. Its interpretation depends on the organism and genomic region.

### 3. DNA Transcription

During transcription, RNA is produced using a DNA template. This project creates a simplified RNA-like sequence by replacing T with U, assuming the input represents the coding strand written in the 5′ to 3′ direction. It does not simulate the complete transcription process.

### 4. Reverse Complement

DNA strands are complementary: A pairs with T and G pairs with C. To calculate the reverse complement, each nucleotide is replaced by its complementary base and the resulting sequence is reversed.

Reverse complements are useful when examining DNA sequences in opposite orientations.

## Testing

The project includes automated tests for:

- Valid DNA sequences
- Invalid characters
- Lowercase input
- Empty input

Run the tests from the project folder:

```bash
python -m unittest discover -s tests
```

A successful run should report four tests and `OK`.

## Future Improvements

- Calculate nucleotide frequencies
- Analyze sequences from FASTA files
- Identify start and stop codons
- Translate coding sequences into amino acid sequences
- Add visualizations of nucleotide composition
- Explore publicly available biological sequence datasets

## Learning Objectives

This project is designed to practise:

- Python functions and dictionaries
- String manipulation
- Input validation and error handling
- Basic software testing
- Version control with Git and GitHub
- Fundamental concepts in molecular biology and bioinformatics

## Author

Biotechnology undergraduate student exploring Python programming and bioinformatics.
