"""
Raj Kumar
CSE 163 AB

Implements the Scraper class to webscrape through Tweet Congress's
dynamically produced website with representative tweets.
"""
from selenium import webdriver
from wordcloud import STOPWORDS
import pandas as pd
import time
import re


class Scraper:
    """
    Represents a webscraper to scrape through a given Tweet Congress URL
    through a specified date range and chrome driver path.
    """
    def __init__(self, url, chrome_driver_location):
        """
        Initializes a Scraper class to store the URL and chrome driver path.
        Has functionality to scrape a given Tweet Congress URL in a specified
        date range.
        """
        self._url = url
        self._chrome_driver_location = chrome_driver_location
        self._df = None

    def get_url(self):
        """
        Getter method for the URL field.
        """
        return self._url

    def get_chrome_driver_location(self):
        """
        Getter method for the chrome driver path field.
        """
        return self._chrome_driver_location

    def get_dataframe(self):
        """
        Getter method for the DataFrame field.
        """
        return self._df

    def _clean_text(self, text):
        """
        Cleans given text by removing emojis, symbols and lowering
        the case.
        """
        text = re.sub(r'http\S+', '', text)
        text = text.lower()
        text_words = text.split()

        filtered_words = [word for word in
                          text_words if word not in STOPWORDS]
        text = ' '.join(filtered_words)
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"
                                   u"\U0001F300-\U0001F5FF"
                                   u"\U0001F680-\U0001F6FF"
                                   u"\U0001F1E0-\U0001F1FF"
                                   "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)
        text = text.strip()
        return text

    def scrape(self):
        """
        Scrapes tweets from a specified date range in a Tweet Congress URL.
        Constructs a DataFrame of tweet IDs, representative names, parties,
        states, respective tweet and the date of tweet.
        """
        driver = webdriver.Chrome(self._chrome_driver_location)
        driver.get(self._url)
        driver.maximize_window()
        for i in range(35000):
            driver.execute_script(
               "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.01)
        ids = driver.find_elements_by_xpath("//*[contains(@id,'t_')]")

        tweet_list = []

        for id in ids:
            tweet_id = id.get_attribute('id')

            rep_name = driver.find_elements_by_xpath(
                '//*[@id="' + tweet_id + '"]/div/div/div/div[2]/div/h2/a')[0]
            name = rep_name.get_attribute('title')

            rep_loc = driver.find_elements_by_xpath(
                '//*[@id="' + tweet_id + '"]/div/div/div/div[1]/div')[0]
            loc = rep_loc.text
            party = loc[0]
            state = loc[2:]

            rep_text = driver.find_elements_by_xpath(
                '//*[@id="' + tweet_id + '"]/div/div/div/div[2]/p[2]')[0]
            text = rep_text.text
            text = self._clean_text(text)

            rep_date = driver.find_elements_by_xpath(
                '//*[@id="' + tweet_id + '"]/div/div/div/div[2]/p[1]')[0]
            date = rep_date.text

            tweet_item = {
                'tweet_id': tweet_id,
                'name': name,
                'party': party,
                'state': state,
                'text': text,
                'date': date
            }

            tweet_list.append(tweet_item)

        self._df = pd.DataFrame(tweet_list)

        driver.quit()

    def display_to_console(self):
        """
        Prints the populated DataFrame to the console.
        """
        print(self._df)

    def to_csv(self):
        """
        Sends the DataFrame to a csv file
        """
        self._df.to_csv('tweet_data', index=False)
