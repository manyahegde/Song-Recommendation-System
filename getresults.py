import pickle
import math
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


dataset = []

client_id = 'bc8b48e76e65439eb21ad4360e105407'
client_secret = '58856e39cebd46bebe021b13d5660c44'
client_credentials_manager = None
spotify = None

def connect_to_spotify():
	global client_credentials_manager
	global spotify
	client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
	spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	print("Successfully connected to spotify")


def read_dataset():
	global dataset
	with open("./dataset.pickle","rb") as f:
		dataset = pickle.load(f)
	print("Dataset read successfully")

def euclidean_distance(sample, list_of_lists):
    distances = {}
    
    for index, lst in enumerate(list_of_lists):
        sample=[float(i) for i in sample]
        lst[3:]=[float(i) for i in lst[3:]]
        if len(sample) != len(lst[3:]):
            raise ValueError("Sample and lists in the list of lists must have the same dimension.")
        
        # Compute the Euclidean distance between the sample and the current list
        distance = math.sqrt(sum((x - y) ** 2 for x, y in zip(sample, lst[3:])))
        
        distances[index] = distance
    
    return distances

def get_nearest_lists(distances, list_of_lists, k=10, num_elements=3):
    # Sort distances dictionary based on increasing distances
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    
    # Get the indices of the lists for the first k nearest distances
    nearest_indices = [index for index, _ in sorted_distances[:k]]
    
    # Get the first 'num_elements' elements from each of the nearest lists
    nearest_elements = [list_of_lists[index][:num_elements] for index in nearest_indices]
    
    return nearest_elements

def get_song_recommendation(sample):
    distance_dict = euclidean_distance(sample, dataset)
    recommendations = get_nearest_lists(distance_dict, dataset, k=10, num_elements=3)
    recommended_songs = []

    for i in recommendations:
        res = get_song_details(i[0])
        song_name = res['Song Name']
        artist_name = res['Artist']
        album_name = res['Album']
        recommended_songs.append([song_name, artist_name, album_name])

    return recommended_songs


# Function to get song details from track ID
def get_song_details(track_id):
    try:
        # Get the track information
        track = spotify.track(track_id)
       
        # Extract relevant details
        song_name = track['name']
        artist = track['artists'][0]['name']
        album = track['album']['name']
        release_date = track['album']['release_date']
        duration_ms = track['duration_ms']
       
        return {
            'Song Name': song_name,
            'Artist': artist,
            'Album': album,
            'Release Date': release_date,
            'Duration (ms)': duration_ms
        }
    except spotipy.exceptions.SpotifyException:
        print('Error: Invalid Track ID')
        return None


read_dataset()
connect_to_spotify()