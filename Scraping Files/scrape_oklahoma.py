import pandas as pd
from helper_functions import get_soup, clean_ou_names
import sqlalchemy

# engine_string = 'mysql+mysqlconnector://root:password@localhost:3306/professorswork'
# engine = sqlalchemy.create_engine(engine_string, echo=True)

soup = get_soup('https://www.ou.edu/cas/history/people/faculty')

name_divs = soup.find_all('div', {'class': 'parbase section textimage'})

prof_info = {
    'profName':[clean_ou_names(nd, 'b') for nd in name_divs],
    # 'titles':
}

print(prof_info)