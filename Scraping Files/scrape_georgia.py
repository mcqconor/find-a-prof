import pandas as pd
from helper_functions import get_soup
import sqlalchemy

engine_string = 'mysql+mysqlconnector://root:password@localhost:3306/professorswork'
engine = sqlalchemy.create_engine(engine_string, echo=True)
soup = get_soup("https://history.uga.edu/directory/faculty")
profs = soup.find_all('strong',{'class':'field-content'})
titles = soup.find_all('div',{'class':'views-field views-field-field-job-title'})

prof_info = {
    'profName':[names.find('h3').text.strip() for names in profs],
    'titles':[title.find('em',{'class':'field-content util-color-olympic'}).text for title in titles],
    'profLink':[''.join(['https://history.uga.edu/',links.find('a',href=True)['href']]) for links in profs]
}

prof_info['institution'] = 'University of Georgia'
prof_info['specialties'] = ''

df = pd.DataFrame.from_dict(prof_info)
df.to_sql('professors', engine, if_exists='append', index=False)