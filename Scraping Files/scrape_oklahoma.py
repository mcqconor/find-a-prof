import pandas as pd
from helper_functions import get_soup, clean_ou_names
import sqlalchemy

engine_string = 'mysql+mysqlconnector://root:password@localhost:3306/professorswork'
engine = sqlalchemy.create_engine(engine_string, echo=True)

soup = get_soup('https://www.ou.edu/cas/history/people/faculty')

name_divs = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['text'])[:-3]

prof_info = {
    'profName':[clean_ou_names(nd, 'b') for nd in name_divs],
    'specialties':[nd.text.split('Research:',1)[1].strip() for nd in name_divs],
    'profLink':[''.join(['https://www.ou.edu',nd.find('a', href=True)['href']]) for nd in name_divs]
}

prof_info['titles'] = ''
prof_info['institution'] = 'University of Oklahoma'
df=pd.DataFrame.from_dict(prof_info)
df.to_sql('professors', engine, if_exists='append', index=False)