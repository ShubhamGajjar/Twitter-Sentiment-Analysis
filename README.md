# 🐦 Twitter-Sentiment-Analysis

### Description
**Sentiment analysis on Twitter data using Python.** This project extracts a specified number of recent tweets from a Twitter user (currently configured for 'elonmusk'), cleans the text, calculates **Subjectivity** and **Polarity** scores using **TextBlob**, and visualizes the results.

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
4.  **Data Extraction:** The notebook attempts to load a `login.csv` file, which is an unnecessary step based on the provided code that directly uses hardcoded API credentials. The `FileNotFoundError` in the original notebook can be ignored, or you can comment out the line `log = pd.read_csv('login.csv')` if you plan to clean up the code.

---

4.  Scroll to the bottom, enter a commit message (e.g., "Updated README with project details and setup instructions."), and click **"Commit changes"**.

### IV. Upload the Notebook File

1.  In your `Twitter-Sentiment-Analysis` repository, click the **"Add file"** dropdown.
2.  Select **"Upload files"**.
3.  Drag and drop the **`Twitter_Sentiment_Analysis.ipynb`** file you downloaded from Colab, or click "choose your files" to select it.
4.  Scroll to the bottom to commit the file:
    * **Commit Message (Title):** `Add initial Jupyter Notebook for sentiment analysis`
    * **Description (Optional):** `Uploads the full Colab notebook for the project.`
5.  Click the **"Commit changes"** button.

Your notebook is now live in your new GitHub repository!

***

Would you like me to help you review the Python code in your notebook to make it more robust (e.g., handling the token error or cleaning up the credential storage)?