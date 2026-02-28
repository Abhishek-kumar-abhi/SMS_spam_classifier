import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# make sure required NLTK data is available on every start
# Streamlit Cloud starts with a fresh environment, and the dataset
# downloader sometimes leaves partial packages; performing a direct
# download ensures both `punkt` and its language subdirectories are
# correctly installed.

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)


ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    # ensure tokenizer resource is present just before use
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

@st.cache_resource

def load_artifacts():
    """Load the vectorizer and classification model once and cache them."""
    with open('vectorizer.pkl', 'rb') as f:
        vect = pickle.load(f)
    with open('model.pkl', 'rb') as f:
        m = pickle.load(f)
    return vect, m

# load on first run, subsequent reruns will use cached copies
tfidf, model = load_artifacts()

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # guard against empty input
    if not input_sms or input_sms.strip() == "":
        st.warning("Please enter a message before clicking Predict.")
    else:
        # 1. preprocess
        transformed_sms = transform_text(input_sms)
        # 2. vectorize
        vector_input = tfidf.transform([transformed_sms])
        # 3. predict
        result = model.predict(vector_input)[0]
        # 4. Display
        if result == 1:
            st.header("Spam")
        else:
            st.header("Not Spam")
