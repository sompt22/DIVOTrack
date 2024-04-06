import numpy as np
import os
import ijson
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import random

def calculate_and_save_similarities(track_features, output_dir):
    """
    Calculate similarities, saving results to disk and updating histograms incrementally.
    """
    intra_path = os.path.join(output_dir, "intra_similarities.npy")
    inter_path = os.path.join(output_dir, "inter_similarities.npy")

    # Initialize histograms
    intra_hist, bins = np.histogram([], bins=20, range=(0, 1))
    inter_hist, _ = np.histogram([], bins=20, range=(0, 1))

    track_ids = list(track_features.keys())
    for i, track_id_i in enumerate(track_ids):
        embeddings_i = np.vstack(track_features[track_id_i])  # Stack for a single 2D array per track
        
        # Intra-track similarities
        if embeddings_i.size > 0:
            similarity_matrix = cosine_similarity(embeddings_i)
            intra_similarities = similarity_matrix[np.triu_indices_from(similarity_matrix, k=1)]            
            np.save(intra_path if i == 0 else intra_path, intra_similarities, allow_pickle=False, fix_imports=False)
            intra_hist += np.histogram(intra_similarities, bins=bins)[0]
        
        # Inter-track similarities
        for j, track_id_j in enumerate(track_ids[i+1:]):
            embeddings_j = np.vstack(track_features[track_id_j])
            if embeddings_j.size > 0:
                inter_similarities = cosine_similarity(embeddings_i, embeddings_j).flatten()
                mode = 'wb' if i == 0 and j == 0 else 'ab'
                with open(inter_path, mode) as f:
                    np.save(f, inter_similarities, allow_pickle=False, fix_imports=False)
                inter_hist += np.histogram(inter_similarities, bins=bins)[0]

    return intra_hist, inter_hist, bins

def plot_histograms(intra_hist, inter_hist, bins, output_dir):
    """
    Plot histograms from pre-aggregated bin counts.
    """
    plt.figure(figsize=(14, 6))

    # Intra-track histogram
    plt.subplot(1, 2, 1)
    plt.bar(bins[:-1], intra_hist, width=np.diff(bins), edgecolor='black', alpha=0.7, label='Intra-track')
    plt.title('Intra-track Similarities')
    plt.xlabel('Similarity Score')
    plt.ylabel('Frequency')
    plt.legend()

    # Inter-track histogram
    plt.subplot(1, 2, 2)
    plt.bar(bins[:-1], inter_hist, width=np.diff(bins), edgecolor='black', color='orange', alpha=0.7, label='Inter-track')
    plt.title('Inter-track Similarities')
    plt.xlabel('Similarity Score')
    plt.ylabel('Frequency')
    plt.legend()

    plt.tight_layout()
    histogram_path = os.path.join(output_dir, "similarity_histograms.png")
    plt.savefig(histogram_path)
    plt.close()

def main():
    output_dir = './output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    track_features = {}  # To store feature vectors indexed by 'sequenceID_trackID'
    filename = './demos/association.json'
    
    with open(filename, 'rb') as f:
        for item in ijson.items(f, 'Sequences.item'):
            sequence_id = item['SequenceID']
            for track in item['Tracks']:
                unique_id = f"{sequence_id}_track{track['Track ID']}"
                if unique_id not in track_features:
                    track_features[unique_id] = []
                frame_feature_vector = np.array(track['Feature Vector'])
                track_features[unique_id].append(frame_feature_vector)
    print("Loaded data.")
    
    # Select 50 random unique_ids from the track_features keys
    random_50_keys = random.sample(list(track_features.keys()), min(50, len(track_features)))
    
    # Create a new dictionary with only the selected 50 unique_ids
    selected_track_features = {key: track_features[key] for key in random_50_keys}    

    intra_hist, inter_hist, bins = calculate_and_save_similarities(selected_track_features, output_dir)
    plot_histograms(intra_hist, inter_hist, bins, output_dir)

if __name__ == '__main__':
    main()
