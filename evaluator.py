from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def evaluate_answer(reference, candidate):
    
    emb1 = model.encode(reference, convert_to_tensor=True)
    emb2 = model.encode(candidate, convert_to_tensor=True)

    similarity = util.cos_sim(emb1, emb2)
    score = float(similarity[0][0])

    if score > 0.75:
        result = "Correct"
    elif score > 0.5:
        result = "Partially Correct"
    else:
        result = "Incorrect"

    return score, result