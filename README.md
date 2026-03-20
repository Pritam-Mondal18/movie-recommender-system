# 🎬 Movie Recommender System  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Machine_Learning-Recommendation-orange?style=for-the-badge&logo=scikitlearn">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
</p>

<p align="center">
  🚀 A modern <b>Movie Recommendation System</b> built using Machine Learning + Flask  
</p>
<p>A content-based movie recommendation system that suggests movies similar to the one selected by the user. This project uses machine learning, Flask, and TMDB API to provide real-time recommendations with movie posters.</p>


---

## 🌐 Live Demo

🔗 **Try it here:**  
👉 https://movie-recommender-system-mmvn.onrender.com  
> ⚠️ Before use this link turn on your VPN, because TMDB API is not working in India.
---

## ✨ Features

- 🎯 Content-based movie recommendation  
- 🧠 Cosine similarity ML model  
- 🖼️ Real-time movie posters using TMDB API  
- 🎨 Modern responsive UI  
- 📱 Mobile + Desktop optimized  
- ⚡ Fast recommendations using precomputed similarity  

---

## 🖼️ Preview

<p align="center">
  <img src="https://via.placeholder.com/800x400?text=Movie+Recommender+UI" width="80%">
</p>

---

## 🛠️ Tech Stack

| Category        | Technology |
|----------------|-----------|
| 💻 Frontend     | HTML, CSS |
| ⚙️ Backend      | Flask (Python) |
| 🤖 ML Model     | Scikit-learn |
| 📊 Data         | Pandas |
| 🌐 API          | TMDB API |
| ☁️ Deployment   | Render |

---

## ⚙️ How It Works

1. Movie dataset is processed and cleaned  
2. Features (cast, crew, genres) are extracted  
3. Data is converted into vectors  
4. Cosine similarity is calculated  
5. Similarity matrix is stored (`similarity.pkl`)  
6. User selects a movie  
7. Top similar movies are recommended  
8. Posters are fetched via TMDB API  

---

## 📂 Project Structure
```
movie-recommender-system/
│
├── templates/
│ └── index.html
│
├── movie_dict.pkl
├── similarity.pkl (as its large file, it works using Google Drive)
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```
---

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv

```
#### Activate:
```bash
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the Application(locally)
```bash
python app.py
```
### Open browser:
```bash
http://127.0.0.1:5000/
```
---
### 🔑 API Setup
#### Get your TMDB API key:

👉 https://www.themoviedb.org/settings/api

#### Replace in app.py:
```bash
api_key = "YOUR_API_KEY"
```
---
### 📈 Future Enhancements

- 🔍 Search with autocomplete
- 🎬 Trailer integration
- ⭐ Ratings & overview
- ⚡ Docker deployment

---
### 👨‍💻 Author

Pritam Mondal

🚀 AI & Full Stack Enthusiast

💡 Passionate about ML & Web Development

---

### ⭐ If you like this project

Give it a ⭐ on GitHub.
