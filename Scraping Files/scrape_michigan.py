import pandas as pd
from helper_functions import get_soup
import sqlalchemy

engine_string = 'mysql+mysqlconnector://root:password@localhost:3306/professorswork'
engine = sqlalchemy.create_engine(engine_string, echo=True)

soup = get_soup('https://lsa.umich.edu/history/people/faculty.directory.html')

name_divs = soup.find_all('div', {'class': 'col-sm-5 col-xs-12'})

prof_info = {
    'profName':[nd.find('a').text for nd in name_divs],
    'titles':[nd.find('span').text for nd in name_divs],
    'profLink':[''.join(['https://lsa.umich.edu/',nd.find('a', href=True)['href']]) for nd in name_divs]
}

areas_of_interest = soup.find_all('p', {'class': 'fields'})

specialties = []
for aoi in areas_of_interest:
    specials = [x.text for x in aoi.find_all('a')]
    specials.remove('History')
    if len(specials) > 1:
        specials = '; '.join(specials)
    elif len(specials) == 0:
        specials = ''
    else:
        specials = specials[0]

    specialties.append(specials)

prof_info['specialties'] = specialties
prof_info['institution'] = 'University of Michigan'
df=pd.DataFrame.from_dict(prof_info)
df.to_sql('professors', engine, if_exists='append', index=False)