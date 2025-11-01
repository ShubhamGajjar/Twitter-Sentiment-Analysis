# 🐦 Twitter-Sentiment-Analysis

### Description
**Sentiment analysis on Twitter data using Python.** This project extracts a specified number of recent tweets from a Twitter user, cleans the text, calculates **Subjectivity** and **Polarity** scores using **TextBlob**, and visualizes the results.

---

### Project Files
* **`Twitter_Sentiment_Analysis.ipynb`**: The main Jupyter Notebook containing all the Python code for data extraction, cleaning, analysis, and visualization.

### Key Libraries Used
* **`tweepy`**: To connect to the Twitter API and extract tweets.
* **`textblob`**: For calculating the sentiment (polarity and subjectivity).
* **`wordcloud`**: For generating a word cloud visualization of the most frequent words.
* **`pandas` & `numpy`**: For data manipulation and storage.
* **`matplotlib`**: For plotting and visualizing the sentiment results.

### Setup and Requirements
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ShubhamGajjar/Twitter-Sentiment-Analysis.git](https://github.com/ShubhamGajjar/Twitter-Sentiment-Analysis.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install tweepy textblob wordcloud pandas matplotlib
    ```
3.  **API Credentials:** The notebook requires Twitter API keys (Consumer Key, Consumer Secret, Access Token, Access Token Secret). **You must replace the placeholder values in the notebook with your own valid keys** for the tweet extraction cell to work.