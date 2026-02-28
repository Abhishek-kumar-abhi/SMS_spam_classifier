mkdir -p ~/.streamlit/

# ensure necessary NLTK corpora are available before the app starts
python -m nltk.downloader punkt stopwords

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml