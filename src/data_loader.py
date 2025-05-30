# src/data_loader.py
import pandas as pd
import os
from src.config import NEWS_RAW_PATH, STOCK_DATA_DIR, STOCK_TICKERS

def load_news_data():
    """
    Loads the raw news data from the specified path.
    Assumes CSV format with 'headline', 'url', 'publisher', 'date', 'stock' columns.
    """
    try:
        df = pd.read_csv(NEWS_RAW_PATH)
        print(f"Successfully loaded news data from: {NEWS_RAW_PATH}")
        print(f"News data shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: News data file not found at {NEWS_RAW_PATH}")
        return None
    except Exception as e:
        print(f"An error occurred while loading news data: {e}")
        return None

def load_all_stock_data():
    """
    Loads historical stock data for all specified tickers.
    Returns a dictionary where keys are tickers and values are DataFrames.
    """
    all_stock_dfs = {}
    for ticker in STOCK_TICKERS:
        file_name = f"{ticker}_historical_data.csv"
        file_path = os.path.join(STOCK_DATA_DIR, file_name)
        try:
            df = pd.read_csv(file_path)
            # Ensure 'Date' is datetime and set as index here for consistency
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            df.dropna(subset=['Date'], inplace=True)
            df.set_index('Date', inplace=True)
            all_stock_dfs[ticker] = df
            print(f"Successfully loaded stock data for {ticker} from: {file_path}")
            print(f"  Shape: {df.shape}")
        except FileNotFoundError:
            print(f"Warning: Stock data file for {ticker} not found at {file_path}. Skipping.")
        except Exception as e:
            print(f"An error occurred while loading stock data for {ticker}: {e}")

    return all_stock_dfs

if __name__ == '__main__':
    # This block runs only when data_loader.py is executed directly
    # Can be used for quick testing of data loading
    news_df = load_news_data()
    if news_df is not None:
        print("\nNews Data Head:")
        print(news_df.head())
        print("\nNews Data Info:")
        news_df.info()

    all_stock_dfs = load_all_stock_data()
    if all_stock_dfs:
        print(f"\nLoaded data for {len(all_stock_dfs)} companies:")
        for ticker, df in all_stock_dfs.items():
            print(f"\nStock Data Head for {ticker}:")
            print(df.head())
            print(f"\nStock Data Info for {ticker}:")
            df.info()
    else:
        print("\nNo stock data was loaded.")