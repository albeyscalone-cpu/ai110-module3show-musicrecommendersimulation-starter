import csv
from dataclasses import asdict, dataclass
from typing import Dict, List, Tuple

NUMERIC_FIELDS = {
    "energy",
    "tempo_bpm",
    "valence",
    "danceability",
    "acousticness",
}

GENRE_WEIGHT = 2.0
MOOD_WEIGHT = 1.5
ENERGY_WEIGHT = 1.0
VALENCE_WEIGHT = 0.75
ACOUSTIC_WEIGHT = 0.5

DEFAULT_WEIGHTS = {
    "genre": GENRE_WEIGHT,
    "mood": MOOD_WEIGHT,
    "energy": ENERGY_WEIGHT,
    "valence": VALENCE_WEIGHT,
    "acoustic": ACOUSTIC_WEIGHT,
}

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top songs for a user profile."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "valence": 0.8,
            "likes_acoustic": user.likes_acoustic,
        }
        scored = []
        for song in self.songs:
            score, _ = score_song(user_prefs, asdict(song))
            scored.append((song, score))
        return [song for song, _ in sorted(scored, key=lambda item: item[1], reverse=True)[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain how one song scored for a user profile."""
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "valence": 0.8,
            "likes_acoustic": user.likes_acoustic,
        }
        score, reasons = score_song(user_prefs, asdict(song))
        return f"Score {score:.2f}: " + "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric fields."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["id"] = int(row["id"])
            for field in NUMERIC_FIELDS:
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(
    user_prefs: Dict,
    song: Dict,
    weights: Dict[str, float] | None = None,
) -> Tuple[float, List[str]]:
    """Score one song against user preferences and explain the score."""
    active_weights = DEFAULT_WEIGHTS.copy()
    if weights:
        active_weights.update(weights)

    score = 0.0
    reasons = []

    if song["genre"].lower() == user_prefs["genre"].lower():
        score += active_weights["genre"]
        reasons.append(f"genre match (+{active_weights['genre']:.2f})")

    if song["mood"].lower() == user_prefs["mood"].lower():
        score += active_weights["mood"]
        reasons.append(f"mood match (+{active_weights['mood']:.2f})")

    energy_score = max(0.0, 1 - abs(song["energy"] - user_prefs["energy"]))
    score += energy_score * active_weights["energy"]
    reasons.append(f"energy closeness (+{energy_score * active_weights['energy']:.2f})")

    target_valence = user_prefs.get("valence", 0.5)
    valence_score = max(0.0, 1 - abs(song["valence"] - target_valence))
    score += valence_score * active_weights["valence"]
    reasons.append(f"valence closeness (+{valence_score * active_weights['valence']:.2f})")

    likes_acoustic = user_prefs.get("likes_acoustic", False)
    acoustic_match = song["acousticness"] >= 0.5 if likes_acoustic else song["acousticness"] < 0.5
    if acoustic_match:
        score += active_weights["acoustic"]
        reasons.append(f"acoustic preference match (+{active_weights['acoustic']:.2f})")

    return round(score, 2), reasons

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
    weights: Dict[str, float] | None = None,
) -> List[Tuple[Dict, float, str]]:
    """Score every song and return the top k ranked recommendations."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song, weights=weights)
        scored.append((song, score, "; ".join(reasons)))

    return sorted(scored, key=lambda item: item[1], reverse=True)[:k]
