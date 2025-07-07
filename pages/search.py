"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
class DuckDuckGoSearchPage:

    # URL
    URL = 'https://duckduckgo.com/'
    
    # Locators
    # locator for the search input field
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    # locator for the search button
    SEARCH_BUTTON = (By.ID, 'search_button_homepage')


    # This module contains DuckDuckGoSearchPage,
    # the page object for the DuckDuckGo search page.
    # It provides methods to load the search page and perform searches.
    # initialization, it takes a browser instance as an argument,
    # which is used to interact with the web page.
    def __init__(self, browser):
        self.browser = browser

#load method is used to navigate to the DuckDuckGo search page.
# It does not take any arguments and does not return anything.
    def load(self):
      self.browser.get(self.URL)
      # Wait for the page to load
      self.browser.implicitly_wait(10)  # Adjust the wait time as needed
      pass

# The search method is used to perform a search on the DuckDuckGo search page.
# It takes a phrase as an argument, which is the search term to be used.
    def search(self, phrase):
        # Find the search input field and enter the search phrase
        # why * is used here?
        # The * operator is used to unpack the tuple returned by the locator.
        # This allows us to pass the locator as separate arguments to the find_element method.
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        
        # Submit the search form
        search_input.send_keys(Keys.RETURN)
        
        # Wait for the results to load
        self.browser.implicitly_wait(10)
        pass