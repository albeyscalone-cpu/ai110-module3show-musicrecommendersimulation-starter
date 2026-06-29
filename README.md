# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

My version will simulate a small content-based music recommender. Instead of
using millions of real user actions like a streaming app, it will compare a
listener's taste profile to each song's stored features and rank the closest
matches with a clear explanation.

---

## How The System Works

Real recommendation platforms combine many signals. Collaborative filtering
looks for patterns in what similar users liked, skipped, replayed, saved, or
added to playlists. Content-based filtering looks at the item itself, such as a
song's genre, mood, tempo, energy, or acousticness. This project will focus on a
simple content-based version so the scoring rule is easy to inspect.

Each `Song` will use these features from `data/songs.csv`: title, artist, genre,
mood, energy, tempo_bpm, valence, danceability, and acousticness. The
`UserProfile` will store a favorite genre, favorite mood, target energy, and
whether the listener likes acoustic songs.

My starting algorithm recipe is:

- Add strong points when the song genre matches the user's favorite genre.
- Add medium points when the song mood matches the user's favorite mood.
- Add similarity points when the song's energy is close to the user's target
  energy, instead of only rewarding high-energy songs.
- Later, rank all songs from highest score to lowest score and return the top
  results with reasons.

Expected bias: because this is a small catalog, the system may over-favor genres
or moods that appear more often. It also cannot understand lyrics, culture,
listening context, or the way a person's taste changes over time.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



