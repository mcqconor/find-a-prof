import pandas as pd
from helper_functions import get_soup, clean_ou_names
import sqlalchemy

# engine_string = 'mysql+mysqlconnector://root:password@localhost:3306/professorswork'
# engine = sqlalchemy.create_engine(engine_string, echo=True)

soup = get_soup('https://www.txst.edu/history/people/faculty-staff.html?')

print([nd.text for nd in soup.find_all('div',{'class':'listitem-title '})])