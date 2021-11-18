mkdir -p ~/.Streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = true\n\
headless = true\n\
\n\
" > ~/.Streamlit/config.toml