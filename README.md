# SMS/Email Spam Classifier

Application URL: https://smsspamclassifierabhi.streamlit.app/

This repository contains a simple machine learning application that classifies text messages (SMS or email) as **spam** or **not spam**. The model and vectorizer are pre-trained and stored as pickled objects, while the front end is a Streamlit app located in `app.py`.

---

## 🚀 Deployment

The application is ready for deployment to **Streamlit Cloud** (previously Streamlit Sharing) or any other platform that supports running Python web apps.

### Requirements
- `Python 3.9` (specified in `runtime.txt`)
- Dependencies listed in `requirements.txt`.

### Local testing
```bash
pip install -r requirements.txt
streamlit run app.py
```

The `setup.sh` script configures Streamlit and downloads necessary NLTK corpora. On the first run the app will also attempt to download the `punkt` and `stopwords` packages if they are missing.

### Streamlit Cloud / Heroku
1. Push the repository to GitHub.
2. Create a new app on [Streamlit Cloud](https://streamlit.io/cloud) and point it at the repo.
3. You can optionally use the provided `Procfile` for Heroku deployment, which runs `sh setup.sh && streamlit run app.py`.

Once deployed the app will be available at a public URL, and users can enter messages and click **Predict** to check for spam.

---

## 🛠️ Project structure

```
app.py              # Streamlit application
vectorizer.pkl      # TF-IDF vectorizer
model.pkl           # trained classifier
requirements.txt    # Python dependencies
setup.sh            # Streamlit configuration (CORS/port) + NLTK downloads
Procfile            # start command for Heroku/Streamlit
runtime.txt         # Python version
README.md           # this file
sms-spam-detection.ipynb  # notebook used for training
spam.csv            # dataset
templates/          # unused in the current version
```

Feel free to retrain or improve the model by editing the notebook.
