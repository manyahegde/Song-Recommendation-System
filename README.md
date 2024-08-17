# Song Recommendation Project

A Flask application that recommends songs using Spotify's Web API.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/chethanarkini/Song_Recommendation_System.git
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
3. **Configure Spotify API**:
Update getresults.py with your Spotify client_id and client_secret.   
4. Run the Application:
   ```bash
   python app.py

## Usage

- Open `http://localhost:56015` in a web browser.
- Submit song features to get recommendations.

## Project Structure

- `app.py`: Flask application
- `getresults.py`: Functions for Spotify and recommendations
- `dataset.pickle`: Dataset file
- `requirements.txt`: Dependencies
- `template/`: HTML templates
