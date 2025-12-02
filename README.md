
# 🔥 Hybrid Tinder-Style Match Recommendation System (Python)

This project implements a **hybrid recommendation system** inspired by social/dating apps like Tinder.  
It intelligently ranks match suggestions using **content-based filtering**, **collaborative filtering**, **social-graph analysis**, and **location proximity**.

The system outputs the **top recommended matches for each user** based on combined weighted similarity scores, and exports a full similarity matrix (`combined_score.csv`).

---

## 🚀 Features

### ✔ Content-Based Filtering (Interests Similarity)
Uses **Jaccard similarity** on user interests such as:
- music  
- movies  
- hiking  
- coding  
- gaming  
- travel  
- photography  
and more.

### ✔ Collaborative Filtering (Swipe Behavior Similarity)
Swipe matrix (0/1) is used to compute:
- **Cosine similarity of user swiping patterns**
- Shows how similar two users' actions are

### ✔ Social Graph Influence (Mutual Friends)
A social adjacency matrix represents connections between users.  
The system computes:
- Mutual friend count  
- Normalizes it to create a **social score**

### ✔ Geographical Distance Score
Users located closer get higher match probability:  
```

distance_score = 1 - (distance_difference / max_distance)

```

### ✔ Hybrid Weighted Score
Final recommendation score is a weighted blend:

```

Combined Score =
0.45 * Content Similarity +
0.25 * Collaborative Similarity +
0.20 * Social Score +
0.10 * Distance Score

```

You can adjust weights anytime.

---

## 🧮 Technologies Used

- Python 3.x
- Numpy  
- Pandas  
- Math  
- Jaccard Similarity  
- Cosine Similarity  

---

## 📁 Project Structure

```

hybrid_recommender/
│
├── hybrid_tinder_recommender.py     # Main script
├── combined_score.csv               # Exported similarity matrix
└── README.md                        # Documentation

````

---

## 🧠 How It Works — Step by Step

### 1️⃣ Define Users & Interests
Users U1–U5 have interest sets:
```python
interests = {
  'U1': {'music','movies','hiking','coding'},
  'U2': {'music','cooking','travel','coding'},
  ...
}
````

### 2️⃣ Content Similarity

Uses **Jaccard similarity**:

```
|intersection| / |union|
```

### 3️⃣ Collaborative Similarity (Swipe Patterns)

Swipe matrix:

```
0 = no swipe
1 = swipe/interaction
```

Cosine similarity compares user behavior.

### 4️⃣ Social Adjacency (Mutual Friends)

```
1 = connected
0 = not connected
```

Mutual connections → normalized social score.

### 5️⃣ Distance Score

Users have assigned distances like:

```
U1: 5 km, U2: 3 km, U3: 12 km ...
```

Closer users = better match %.

### 6️⃣ Hybrid Weighted Score

All four scores are combined using:

```python
combined_score = (w_content * content_sim +
                  w_collab * collab_sim +
                  w_social * social_score +
                  w_distance * distance_score)
```

### 7️⃣ Top-N Recommendations

Top 3 recommendations printed for each user:

```python
recommend_for_user("U1")
```

### 8️⃣ Output Screenshots


<img width="900" height="1000" alt="image" src="https://github.com/user-attachments/assets/d671d012-76ad-45e0-9f35-762be2a4fd23" />




## ▶️ Running the Program

### 1. Install dependencies

```bash
pip install numpy pandas
```

### 2. Run the script

```bash
python hybrid_tinder_recommender.py
```

### 3. Output

* Shows **top recommendations** for each user
* Saves **combined_score.csv** in the project folder

---

## 📄 Example Output

```
Top Recommendations for Each User:

User U1 ->
U5    0.723
U2    0.615
U4    0.588
```

*(Values shown are for illustration)*

---

## 📌 Customization

You can easily modify:

### ✔ Weights

Inside the script:

```python
w_content = 0.45
w_collab = 0.25
w_social = 0.20
w_distance = 0.10
```

### ✔ Users

### ✔ Interests

### ✔ Swipe Matrix

### ✔ Social Network

### ✔ Distance in KM

---

## 🌟 Future Improvements

* Add **ML-based preference learning**
* Add visualizations (heatmaps, graphs)
* Build a **web UI** or **mobile app**
* Use real GPS location logic
* Introduce age, gender, and bio similarity features


