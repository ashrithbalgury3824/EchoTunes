# 🎶 Echo Tunes – AIML-Based Music Recommendation System  

Echo Tunes is an **AI/ML-powered music recommendation system** designed to provide personalized song suggestions based on **mood, genre, and language preferences**.  
The project combines **content-based filtering**, **user behavior analysis**, and integration with the **Spotify API (via Spotipy)** to deliver smart, real-time music recommendations.  

---

## ✨ Features  
- 🎼 **Personalized Playlists** – Songs recommended based on mood, genre, and language.  
- 🤖 **Machine Learning Models** – Uses algorithms like Random Forests, SVM, and Neural Networks for accurate predictions.  
- 🎧 **Spotify API Integration** – Expands recommendations using Spotify’s vast library via Spotipy.  
- 🎚️ **Dynamic Filtering** – Supports mood-based, genre-based, and language-specific discovery.  
- 🔄 **Iterative Refinement** – Continuously learns and improves recommendations from user feedback.  

---

## 📂 Project Structure  

```text
Echo-Tunes/
│-- data/                # Custom CSV dataset (initial recommendation system)  
│-- models/              # ML models and training scripts  
│-- notebooks/           # Jupyter notebooks for experiments & testing  
│-- src/                 # Core project code (recommendation engine, Spotify API integration)  
│-- requirements.txt     # Python dependencies  
│-- README.md            # Project documentation
---
```

## 🛠️ Tech Stack  
- **Languages**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn, TensorFlow/Keras  
- **API**: Spotify Web API (via Spotipy)  
- **Visualization**: Matplotlib, Seaborn  

---

## 📊 Dataset  
- **Music Library Dataset** – Used for initial testing (custom CSV).  
- **Spotify API Data** – Provides real-time recommendations and expanded metadata.  

---

## ⚙️ Installation & Setup  

1. Clone the repository:  
   ```bash
   git clone https://github.com/ashrithbalgury3824/echo-tunes.git
   cd echo-tunes
   
2. Create a virtual environment and install dependencies:
   pip install -r requirements.txt

3. Run the app:
   python src/app.py

📖 Usage

- Select mood, genre, and language.

- Get personalized recommendations from both the custom dataset and Spotify API.

- Explore new songs while receiving continuous learning-based suggestions.

👨‍💻 Team Members

- Balgury Ashrith Rao (2320030442)

- Shrot Kumar Pandey (2320030448)

- Adithya Kiran Goud Thigulla (2320030498)

📌 Future Improvements

- Add collaborative filtering for social playlist sharing.

- Mobile app integration.

- More advanced deep learning models for genre/mood detection.
