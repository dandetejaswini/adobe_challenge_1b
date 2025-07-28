import fitz  # PyMuPDF
import json
import os
from datetime import datetime
from utils import rank_sections, extract_subsections


def analyze_documents(input_folder, persona, job, output_path):
    results = {
        "metadata": {
            "input_documents": os.listdir(input_folder),
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": str(datetime.now())
        },
        "extracted_sections": [],
        "sub_section_analysis": []
    }

    for doc_name in os.listdir(input_folder):
        print(f"Processing: {doc_name}")
        path = os.path.join(input_folder, doc_name)

        try:
            doc = fitz.open(path)
        except Exception as e:
            print(f"Could not open {doc_name}: {e}")
            continue

        for page_number, page in enumerate(doc):
            text = page.get_text("text")
            if not text.strip():
                continue  # Skip empty pages

            sections = text.split('\n\n')  # Naive section split
            ranked = rank_sections(sections, persona, job)

            for i, (section, score) in enumerate(ranked):
                results["extracted_sections"].append({
                    "document": doc_name,
                    "page_number": page_number + 1,
                    "section_title": section.strip()[:50],
                    "importance_rank": i + 1
                })

                refined = extract_subsections(section, persona, job)
                results["sub_section_analysis"].append({
                    "document": doc_name,
                    "page_number": page_number + 1,
                    "refined_text": refined
                })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    input_folder = "input_docs"
    output_path = "output/output.json"

    # Example persona + job
    persona = "Tourism Content Creator"
    job = "Create a travel blog guide highlighting top attractions, culture, and local tips for South of France"

    print("Starting document analysis...")
    analyze_documents(input_folder, persona, job, output_path)
    print("Done! Output saved to", output_path)
