# Technical Approach for Persona-Driven Document Analysis

## Objective

The system is designed to extract relevant content from large unstructured PDF documents using a user-defined persona and task (job to be done). The goal is to highlight only the most relevant sections and provide concise summaries.

## Methodology

### 1. Document Reading

We use the `PyMuPDF` library (`fitz`) to read PDF documents page by page. Each page's text is extracted and split into coarse-grained sections using a double newline (`\n\n`) heuristic.

### 2. Section Relevance Scoring

Each section is compared with a combined string: `persona + job`. We use the `TfidfVectorizer` from `scikit-learn` to compute cosine similarity between this context and each section. Sections are ranked by their similarity scores.

### 3. Subsection Extraction

Top-ranked sections (top 5) are further summarized by extracting the top 2–3 lines using a simple rule-based summarization method. This makes the results concise and highlights actionable insights.

### 4. Output Formatting

The extracted information is saved as a structured `output.json` file containing:

- Metadata: Input files, persona, task, timestamp.
- Ranked Sections: Title snippets, page numbers, and ranks.
- Subsection Analysis: Summarized top lines for each relevant section.

## Why This Approach?

- Lightweight and fast: Ideal for environments with resource constraints.
- Domain-agnostic: Works for any persona/task combination without fine-tuning.
- Transparent: Output is easy to interpret and trace back to source documents.
- Compliant: Fits within 1GB memory and 60-second execution time as required.

## Limitations and Future Enhancements

- Current sectioning is heuristic-based and may be improved with NLP-based chunking.
- Summarization is basic; LLM-based summarization (like TextRank or BART) could improve precision.
- Retrieval could be enhanced using dense vector embeddings (e.g., SBERT).

## Dependencies

- `PyMuPDF` for PDF parsing
- `scikit-learn` for TF-IDF and similarity scoring
- `joblib`, `numpy`, `scipy` (required by scikit-learn)

All dependencies are installed using pre-downloaded `.whl` files in the `wheels/` directory.
