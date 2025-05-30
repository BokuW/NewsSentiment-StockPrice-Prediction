# src/config.py
import os

# Define the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Data Paths ---
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw') # Still useful for raw_analyst_ratings.csv
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

NEWS_RAW_FNAME = 'raw_analyst_ratings.csv'
NEWS_RAW_PATH = os.path.join(DATA_DIR, NEWS_RAW_FNAME) 

# Directory for historical stock data
STOCK_DATA_DIR = os.path.join(DATA_DIR, 'yfinance_data')

# List of stock tickers to process
STOCK_TICKERS = ['AAPL', 'AMZN', 'GOOG', 'META', 'NVDA', 'TSLA']

PROCESSED_NEWS_PATH = os.path.join(PROCESSED_DATA_DIR, 'processed_news.pkl')
FEATURES_PATH = os.path.join(PROCESSED_DATA_DIR, 'features.pkl')

# --- Model Paths 
MODELS_DIR = os.path.join(BASE_DIR, 'models')
SENTIMENT_MODEL_PATH = os.path.join(MODELS_DIR, 'sentiment_model.pkl')
STOCK_PREDICTION_MODEL_PATH = os.path.join(MODELS_DIR, 'stock_prediction_model.pkl')

# --- EDA Output Paths 
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')
EDA_OUTPUT_DIR = os.path.join(REPORTS_DIR, 'eda')


# --- Other Configurations ---
RANDOM_SEED = 42
N_TOP_PUBLISHERS = 20 # For EDA
SENTIMENT_THRESHOLD = 0.5 

# Create necessary directories if they don't exist
for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR, REPORTS_DIR, EDA_OUTPUT_DIR, STOCK_DATA_DIR]:
    os.makedirs(directory, exist_ok=True)

print("Project structure setup complete and config.py created/updated.")
print(f"Base Directory: {BASE_DIR}")
print(f"News Raw Path: {NEWS_RAW_PATH}")
print(f"Stock Data Directory: {STOCK_DATA_DIR}")
print(f"Tickers to process: {STOCK_TICKERS}")