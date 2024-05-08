from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from core.recommender.LocationsLoader import LocationsLoader

class Recommender:
    # Preprocess text features
    tfidf = TfidfVectorizer(stop_words='english')

    def __init__(self, locations: LocationsLoader):
        self.locations = locations.get_locations()
        combined_features = self.locations['category'].apply(lambda x: x['name'])
        self.location_features = self.tfidf.fit_transform(combined_features)

        # Calculate cosine similarity matrix
        self.cosine_sim_matrix = cosine_similarity(self.location_features, self.location_features)

    def run(self, location_index, top_n=5):

        # Get the similarity scores for the given Location
        if int(location_index) >= len(self.cosine_sim_matrix):
            similarity_scores = self.cosine_sim_matrix[-1]
        else:
            similarity_scores = self.cosine_sim_matrix[int(location_index)]

        top_indices = similarity_scores.argsort()[::-1][1:top_n+1]

        return self.locations.loc[top_indices, :].to_dict(orient='records')
