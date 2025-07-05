"""
This module contains shared fixtures.
"""

import pytest
# Import the pytest module for creating fixtures and running tests
import selenium.webdriver

# This fixture provides a WebDriver instance for browser automation tests.
# It initializes a ChromeDriver instance, sets an implicit wait time, and ensures
# that the WebDriver instance is properly cleaned up after tests are run.
# une fonction qui comprend à la fois les phases de configuration et de nettoyage dans un seul corps.
@pytest.fixture

def browser():

  # Initialize the ChromeDriver instance
  b = selenium.webdriver.Chrome()

  # Make its calls wait up to 10 seconds for elements to appear
  # This is useful for handling dynamic content that may take time to load
  # evry time an element is searched for, the driver will wait up to 10 seconds
  # before throwing an exception if the element is not found.
  b.implicitly_wait(10)

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit() 