# News Sentiment and Stock Price Prediction

This project explores the relationship between financial news sentiment and stock price movements. It establishes a robust analytical framework to assess whether sentiment signals from news headlines can help explain or predict stock market behavior, focusing on multiple major stocks.

## Key Features

- **End-to-End Pipeline**: From news text preprocessing to technical analysis of stock prices.
- **Sentiment Analysis**: Cleans and analyzes news headlines using NLTK and TextBlob.
- **Quantitative Stock Analysis**: Computes technical indicators (SMA, RSI, MACD, Bollinger Bands, etc.) with TA-Lib and PyNance.
- **Correlation Studies**: Aligns and examines relationships between aggregated news sentiment and daily stock returns.
- **Visualizations**: Includes bar charts for n-gram frequencies, candlestick charts with overlays, and scatter plots for sentiment/return analysis.

## Project Structure

- `src/config.py`: Central location for all configuration (data paths, tickers, ).
- `data/`: Contains raw news and stock price CSVs.
- `notebooks/`: Jupyter notebooks for analysis.
- ` src/__pycache__`
- `.gitignore`
- `requirements`
- `reports/eda`: Contains all EDA plot file
- `.venv/`
- `.github/workflows/unittest.yml`
- `tests`

## Setup & Requirements

1. **Clone the repository** and create a virtual environment:
    ```bash
    git clone https://github.com/yourusername/news-sentiment-stock-prediction.git
    cd news-sentiment-stock-prediction
    python -m venv .venv
    source .venv/bin/activate
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download NLTK corpora** (run once in your notebook or Python shell):
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    ```

## Analysis Workflow

### 1. Exploratory Data Analysis & Preprocessing
- Load news headlines (`raw_analyst_ratings.csv`).
- Clean text: lowercase, remove URLs/punctuation, tokenize, remove stopwords.
- Show most frequent unigrams, bigrams, trigrams.

### 2. Stock Price Analysis
- Load historical price data for target tickers (AAPL, AMZN, GOOG, META, NVDA, TSLA).
- Add technical indicators (SMA, RSI, MACD, Bollinger Bands, etc.).
- Visualize price trends, returns, and volatility.

### 3. Sentiment/Return Correlation
- Align daily news and stock data by date.
- Aggregate sentiment scores and compute average daily sentiment.
- Calculate daily returns and merge with sentiment for correlation analysis.
- Visualize relationships (scatter plots, time series).

## Challenges Addressed

- **NLTK LookupError**: Resolved by explicit corpus download.
- **Module Import Issues**: Fixed by dynamically updating `sys.path` in notebooks.
- **FileNotFound/Syntax/Indentation Errors**: Debugged and corrected data paths and code structure.
- **Data Alignment**: Developed robust datetime handling and alignment for large datasets.
- **Visualization Issues**: Improved plotting logic for clear, sequential chart display.

## Recommendations for Further Work

- Explore lagged and non-linear correlations.
- Integrate additional data (social media, economic indicators).
- Develop and backtest predictive models (e.g., ARIMA, Random Forest, LSTM).

## Conclusion

The initial phase established a solid foundation for news sentiment analysis in relation to stock prices. While simple sentiment measures showed weak linear correlation with daily returns, the infrastructure and insights gained set the stage for deeper, more advanced modeling and prediction.

---

**Author:** [LENCHO URGESSA] 
