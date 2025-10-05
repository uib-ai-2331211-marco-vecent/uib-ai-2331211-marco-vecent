import pandas as pd
import numpy as np

# Buat dataset sederhana 50 film
titles = [f"Movie {i}" for i in range(1, 51)]
avg_rating = np.random.uniform(2.0, 5.0, 50).round(2)
rating_count = np.random.randint(5, 300, 50)

df = pd.DataFrame({
    "title": titles,
    "avg_rating": avg_rating,
    "rating_count": rating_count
})

df.to_csv("movie_sample.csv", index=False)
print("Dataset movie_sample.csv berhasil dibuat!")
print(df.head())
