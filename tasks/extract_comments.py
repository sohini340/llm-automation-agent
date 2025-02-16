from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import itertools
import os

def process():
    """Find the most similar comments in the dataset."""
    input_file = "/data/comments.txt"
    output_file = "/data/comments-similar.txt"

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"{input_file} does not exist")

    # Load the model
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # Read comments
    with open(input_file, "r", encoding="utf-8") as f:
        comments = [line.strip() for line in f.readlines() if line.strip()]

    if len(comments) < 2:
        raise ValueError("Not enough comments to compare similarity.")

    # Generate embeddings
    embeddings = model.encode(comments)

    # Find the most similar pair
    max_similarity = -1
    most_similar_pair = ("", "")

    for (i, comment1), (j, comment2) in itertools.combinations(enumerate(comments), 2):
        similarity = cosine_similarity([embeddings[i]], [embeddings[j]])[0][0]
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_pair = (comment1, comment2)

    # Write to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(most_similar_pair))

    return f"Most similar comments saved to {output_file}"

