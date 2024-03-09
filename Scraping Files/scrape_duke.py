"""
WORK IN PROGRESS
"""
import pandas as pd
from helper_functions import get_soup, find_duke_focus

soup = get_soup('https://history.duke.edu/people/appointed-faculty/primary-faculty')
profs = soup.find_all('article')
names = [find_duke_focus(name, 'div','h4') for name in profs]
print(names)

print([find_duke_focus(title, 'div','h6') for title in profs])