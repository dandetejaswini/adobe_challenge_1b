from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_sections(sections, persona, job):
    context = persona + " " + job
    vect = TfidfVectorizer().fit([context] + sections)
    vectors = vect.transform([context] + sections)
    scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    ranked = sorted(zip(sections, scores), key=lambda x: x[1], reverse=True)
    return ranked[:5]  # top 5 relevant sections

def extract_subsections(section_text, persona, job):
    # Simple summarizer: Keep top 2-3 lines
    lines = section_text.splitlines()
    return "\n".join(lines[:3])
