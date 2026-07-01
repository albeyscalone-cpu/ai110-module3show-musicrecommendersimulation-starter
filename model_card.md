# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

The system works best when a listener's preferences line up clearly with the
catalog. The `Chill Lofi` profile produced results that felt very reasonable:
`Library Rain`, `Midnight Coding`, and `Focus Flow` all matched the expected
genre, calmer energy range, and acoustic feel. The `Deep Intense Rock` profile
also behaved well at the top of the list because `Storm Runner` strongly matched
genre, mood, and energy at the same time.

---

## 6. Limitations and Bias 

This recommender can over-reward numerical similarity even when the genre is not
especially close. For example, `Gym Hero` stayed near the top for both
`High-Energy Pop` and `Deep Intense Rock` because its energy and mood values fit
both profiles well enough to overcome the genre mismatch. The catalog is also
small and uneven, so lofi and pop songs have an advantage simply because there
are more close neighbors for those tastes. It does not consider lyrics, vocals,
language, listening history, or context, so it can miss why two songs with
similar numbers might feel completely different to a human listener.

---

## 7. Evaluation  

I tested three profiles: `High-Energy Pop`, `Chill Lofi`, and `Deep Intense
Rock`. I checked whether the top recommendations changed in a way that matched
the target vibe instead of returning the same few songs every time. The most
interesting result was that the top song usually made sense, but the second and
third recommendations sometimes crossed genre boundaries if their energy and
valence were close enough. I also ran a small experiment where I doubled the
energy weight and cut the genre weight in half. That changed the `High-Energy
Pop` ranking by moving `Rooftop Lights` above `Gym Hero`, which showed that the
system is quite sensitive to the weight choices.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
