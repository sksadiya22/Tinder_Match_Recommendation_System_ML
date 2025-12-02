import numpy as np
import pandas as pd
from math import sqrt

users = ['U1','U2','U3','U4','U5']

interests = {
    'U1': {'music','movies','hiking','coding'},
    'U2': {'music','cooking','travel','coding'},
    'U3': {'anime','gaming','coding'},
    'U4': {'movies','travel','coffee','hiking'},
    'U5': {'music','hiking','travel','photography'}
}

distance_km = {'U1': 5, 'U2': 3, 'U3': 12, 'U4': 7, 'U5': 4}

swipe_matrix = pd.DataFrame(
    [[0,1,0,1,1],
     [1,0,0,1,0],
     [0,0,0,1,0],
     [0,1,1,0,1],
     [1,0,0,1,0]],
    index=users, columns=users, dtype=int
)

social_adj = pd.DataFrame(
    [[0,1,0,1,1],
     [1,0,1,1,0],
     [0,1,0,0,0],
     [1,1,0,0,1],
     [1,0,0,1,0]],
    index=users, columns=users, dtype=int
)

def jaccard_similarity(a, b):
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union > 0 else 0.0

def cosine_similarity(a, b):
    num = np.dot(a, b)
    den = np.linalg.norm(a) * np.linalg.norm(b)
    return num / den if den != 0 else 0.0

content_sim = pd.DataFrame(index=users, columns=users, dtype=float)
for u in users:
    for v in users:
        content_sim.loc[u,v] = 0 if u==v else jaccard_similarity(interests[u], interests[v])

collab_sim = pd.DataFrame(index=users, columns=users, dtype=float)
for u in users:
    for v in users:
        collab_sim.loc[u,v] = 0 if u==v else cosine_similarity(
            swipe_matrix.loc[u].values.astype(float),
            swipe_matrix.loc[v].values.astype(float)
        )

mutual_counts = pd.DataFrame(index=users, columns=users, dtype=float)
for u in users:
    for v in users:
        mutual_counts.loc[u,v] = 0 if u==v else int(((social_adj.loc[u] & social_adj.loc[v]).sum()))

max_mutual = mutual_counts.values.max() if mutual_counts.values.max() > 0 else 1
social_score = mutual_counts / max_mutual

max_dist = max(distance_km.values())
distance_score = pd.DataFrame(index=users, columns=users, dtype=float)
for u in users:
    for v in users:
        if u == v:
            distance_score.loc[u,v] = 0
        else:
            d = abs(distance_km[u] - distance_km[v])
            distance_score.loc[u,v] = max(1 - (d / max_dist), 0)

w_content, w_collab, w_social, w_distance = 0.45, 0.25, 0.20, 0.10

combined_score = (w_content * content_sim +
                  w_collab * collab_sim +
                  w_social * social_score +
                  w_distance * distance_score)

for u in users:
    combined_score.loc[u,u] = -1

def recommend_for_user(user, top_n=3):
    scores = combined_score.loc[user].sort_values(ascending=False)
    return scores.head(top_n)

print("Top Recommendations for Each User:\n")
for u in users:
    print("User " + u + " ->")
    print(recommend_for_user(u), "\n")

combined_score.to_csv("combined_score.csv")
print("Saved: combined_score.csv")
