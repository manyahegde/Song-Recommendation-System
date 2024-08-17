# SoundSafari - Song Recommendation System

## Purpose
SoundSafari is a web application designed to recommend songs to users based on their preferences for various musical attributes. It offers a personalized music recommendation experience by allowing users to specify their preferences, which are then matched against a dataset of songs.

## Technology Stack
- **Backend:** Python with Flask web framework
- **Frontend:** HTML with some JavaScript
- **External API:** Spotify API (using the `spotipy` library)

## Key Features
- **User Interface:** 
  - A web form where users can select preferences for attributes such as:
    - Popularity
    - Duration
    - Explicit Lyrics
    - Danceability
    - Energy
    - Acousticness
    - Valence
    - Tempo
- **Recommendation Engine:** 
  - Utilizes a nearest neighbor algorithm with Euclidean distance to find songs that match the user's preferences.
- **Spotify Integration:** 
  - Fetches additional details about recommended songs using the Spotify API.
- **Results Display:** 
  - Recommended songs are presented with their names, artists, and albums in an attractive card layout.

## How It Works
1. Users input their preferences on the main page.
2. The backend processes these preferences and compares them against a pre-loaded dataset of songs.
3. The system selects the top 10 most similar songs based on the input criteria.
4. Additional details about these songs are fetched from Spotify.
5. The results are displayed on a separate page with a visually appealing interface.

