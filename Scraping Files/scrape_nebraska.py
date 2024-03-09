import pandas as pd
from helper_functions import get_soup, clean_nebraska_links
import sqlalchemy

engine_string = 'mysql+mysqlconnector://root:password@localhost:3306/professorswork'
engine = sqlalchemy.create_engine(engine_string, echo=True)
soup = get_soup('https://history.unl.edu/directory-group')
profs = soup.find_all('div',{'class':'person-info'})

prof_info = {
    'profName':[name.find('h3').text.strip() for name in profs],
    'titles':[title.find('span',{'class':'title'}).text for title in profs],
    'profLink':[clean_nebraska_links(link, 'a') for link in profs]
}

prof_info['institution'] = 'University of Nebraska'
prof_info['specialties'] = ''
df = pd.DataFrame.from_dict(prof_info)
df.to_sql('professors', engine, if_exists='append', index=False)