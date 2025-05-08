# 🕵️ Fake Review Detection System

This is a **Streamlit web application** that detects whether a product or service review is **genuine** or **fake**. The application uses a **Logistic Regression (LR)** model trained on a dataset of real-world reviews to classify the authenticity of user-provided reviews.

---

## 🚀 Features

- **User-Friendly Interface**: Enter a review and get instant feedback on its authenticity.
- **Confidence Score**: Displays the model's confidence in its prediction.
- **Text Preprocessing**: Automatically cleans and preprocesses the input text for analysis.
- **Custom Styling**: A visually appealing design with a dark theme.

---

## 🛠️ How It Works

1. **Input**: The user enters a review in the text area provided.
2. **Preprocessing**: The review is cleaned (removal of HTML tags, punctuation, numbers, etc.) and vectorized using a **TF-IDF Vectorizer**.
3. **Prediction**: The Logistic Regression model predicts whether the review is genuine or fake.
4. **Output**: The result is displayed along with a confidence score.

---

## 🧰 Installation

### Prerequisites

- Python 3.8 or higher
- `pip` package manager

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Reshusingh0702/fake-review-detector.git
   cd fake-review-detector
   ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```

3. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
    streamlit run streamlit_app.py
   ```

## 📁 Project Structure 
```
fake-review-detector/ 
├── streamlit_app.py # Streamlit web application 
├── fake-review-detection_v2.ipynb # Jupyter Notebook for model training 
├── model_v1.pkl # Trained Logistic Regression model 
├── vectorizer_v1.pkl # TF-IDF Vectorizer 
├── requirements.txt # Python dependencies 
└── README.md # Project documentation 
```

## 📊 Dataset
The model was trained on the [Fake Reviews Dataset](./fake-reviews-dataset.csv) from Kaggle. The dataset contains labeled reviews categorized as genuine or fake.


## 🧪 Model Training
The **Logistic Regression** model was trained using the following steps:

   1. Text Preprocessing:

      * Lowercasing
      * Removal of punctuation, numbers, and stopwords
      * Stemming using the Porter Stemmer
   
   2. Feature Extraction:

      * TF-IDF Vectorizer with a maximum of 3000 features.

   3. Model Evaluation:

      * Achieved high accuracy and precision on the test set.
     
   4. Pickling:

      * The trained model and vectorizer were saved as model_v1.pkl and vectorizer_v1.pkl for use in the web application.

## 📦 Dependencies
The following Python libraries are required:

* `streamlit`
* `joblib`
* `scikit-learn`
* `nltk`
* `pandas`
* `numpy`
* `matplotlib`
* `seaborn`
* `wordcloud`
* `xgboost`

## 🖼️ Screenshots

### Genuine review prediction result

![Genuine](./screenshots/Genuine_Review.png)

### Fake review prediction result

![Fake](./screenshots/Fake_Review.png)

## 🔗 Important Links
* **Kaggle Dataset:** [Fake Reviews Dataset](https://www.kaggle.com/datasets/mexwell/fake-reviews-dataset)
* **Streamlit Documentation:** [Streamlit Docs](https://docs.streamlit.io/)
* **GitHub Repository:** [Fake Review Detection System](https://github.com/Reshusingh0702/fake-review-detector)

## 🛠️ Dependency Usage
* **Streamlit:** For building the web application.
* **Scikit-learn:** For training the Logistic Regression model.
* **NLTK:** For text preprocessing.
* **Matplotlib & Seaborn:** For data visualization.
