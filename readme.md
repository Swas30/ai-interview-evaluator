# AI Mock Interview Evaluator

This project simulates a simple AI interview agent that evaluates candidate answers using semantic similarity.

The system compares a candidate's answer with a reference answer using sentence embeddings from Sentence Transformers.

## Features

- Automated answer evaluation
- Semantic similarity scoring
- AI based interview simulation

## Tech Stack

Python  
Sentence Transformers  
Scikit-learn  
Numpy

## How It Works

1. The system asks interview questions.
2. The candidate provides an answer.
3. Both answers are converted into embeddings.
4. Cosine similarity is calculated.
5. The system classifies the answer as correct, partially correct, or incorrect.