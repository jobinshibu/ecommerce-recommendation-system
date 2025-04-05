import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load the cleaned dataset
df = pd.read_csv("Cleaned_OnlineRetail.csv")  # Ensure the correct file path

# Drop missing values in the Description column
df["Description"] = df["Description"].fillna("")

df_unique = df.drop_duplicates(subset=["Description"])


tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix_unique = tfidf.fit_transform(df_unique["Description"])


knn = NearestNeighbors(n_neighbors=5, metric="cosine", algorithm="brute")
knn.fit(tfidf_matrix_unique)

def recommend_products(product_name, df, tfidf_matrix, knn_model, n_recommendations=5):
    try:
        # Find the index of the product
        idx = df[df["Description"].str.lower() == product_name.lower()].index[0]

        # Find nearest neighbors (similar products)
        distances, indices = knn_model.kneighbors(tfidf_matrix[idx], n_neighbors=n_recommendations+1)

        # Get recommended product names (excluding the input product)
        recommended_products = df.iloc[indices[0][1:]]["Description"].values

        return recommended_products
    except IndexError:
        return ["Product not found. Try a different name."]

sample_product = "WHITE METAL LANTERN"
recommendations_fixed = recommend_products(sample_product, df_unique, tfidf_matrix_unique, knn)
print(recommendations_fixed)

