# 📰 Detecting Fake Health News with ML

This project is a machine learning-based system that classifies news as **Real** or **Fake**, specifically focused on Indian health-related news. It uses **TF-IDF Vectorization** and **Logistic Regression** to detect misinformation.

---

## 📁 Project Structure

📦 fake-news-detector/
├── app.py # Main Python script to run the model
├── indian_health_fake_news.csv # Dataset used for training/testing
├── tfidf_vectorizer.pkl # Saved TF-IDF vectorizer
├── fake_news_model.pkl # Trained logistic regression model
└── README.md # Project description and instructions

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/TejaNagaSri13/fake-news-detector.git
cd fake-news-detector
2️⃣ Install Required Libraries
If you don't want to use a requirements.txt file, install manually:
pip install pandas scikit-learn

3️⃣ Run the Script
python app.py
You’ll be able to enter custom news text and the model will predict if it's Real or Fake.

🧪 Required Libraries
To run this project, make sure you have the following Python libraries installed:
pandas
scikit-learn

🧠 Machine Learning Model
Vectorization: TF-IDF (Term Frequency-Inverse Document Frequency)

Classifier: Logistic Regression

Evaluation: Classification Report (Precision, Recall, F1-score)

📊 Dataset
The dataset used is indian_health_fake_news.csv, which contains labeled health-related news articles from Indian sources.

Column	Description
Text	News content
Label	1 = Real, 0 = Fake



👤 Author
Name: Kola Teja Naga Sri

GitHub: TejaNagaSri13

LinkedIn: https://www.linkedin.com/in/teja-nagasri-kola-27a752280


📌 License
This project is open source and available under the MIT License.

