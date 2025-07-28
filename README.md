# Adobe Hackathon Round 1B – Persona-Driven Document Intelligence

## Problem Statement

Design a lightweight system that identifies and extracts the most relevant content from unstructured documents based on a given user persona and their task (job to be done). The goal is to extract relevant sections from PDFs and provide structured output in a machine-readable format.

## Project Structure

```
adobe_1b/
├── app/
│   ├── input_docs/              # Input folder for PDFs
│   ├── output/                  # Stores JSON output
│   ├── processor.py             # Main processing logic: extraction and scoring
│   ├── utils.py                 # Contains TF-IDF scoring and summarization methods
│   └── __pycache__/             # Python cache
├── wheels/                      # Pre-downloaded .whl files (offline packages)
├── run.sh                       # Entry point script to execute processing
├── requirements.txt             # Required Python packages
├── Dockerfile                   # Docker container setup
├── approach_explanation.md     # Technical methodology and decisions
└── README.md                    # Instructions and usage
```

## How to Run

### 1. Install Docker  
Ensure Docker is installed on your machine.

### 2. Build Docker Image

```bash
docker build -t adobe_1b .
```

### 3. Run the Container

```bash
docker run --rm -v $(pwd)/app/input_docs:/app/app/input_docs -v $(pwd)/app/output:/app/app/output adobe_1b
```

This will process the documents in `input_docs` and generate `output.json` in the `output/` folder.

## File Descriptions

- `processor.py`: Main script that reads PDF files, ranks sections based on TF-IDF similarity to persona + task, and writes JSON output.
- `utils.py`: Contains utility functions for TF-IDF-based ranking and extracting top lines from a section.
- `requirements.txt`: Specifies package dependencies like PyMuPDF and scikit-learn.
- `Dockerfile`: Defines the Docker environment.
- `run.sh`: Shell script to create output directory and run the processor.
- `approach_explanation.md`: Documents the end-to-end methodology.

## Input/Output Format

- Input: PDF files inside `app/input_docs/`
- Output: A single `output.json` file inside `app/output/` with metadata, ranked sections, and refined summaries.
