import pandas as pd
from helper_functions import get_soup, find_ucla_focus
import sqlalchemy

engine_string = 'mysql+mysqlconnector://root:password@localhost:3306/professorswork'
engine = sqlalchemy.create_engine(engine_string, echo=True)
soup = get_soup('https://history.ucla.edu/people/faculty/')

links = soup.find_all('div',{'class':'av-special-heading av-special-heading-h2 blockquote modern-quote avia-builder-el-1 el_after_av_table el_before_av_one_fourth'})

area_of_interest = soup.find_all('div', 
                                 {'class':'flex_column av_two_fifth flex_column_div av-zero-column-padding avia-builder-el-3 el_after_av_one_fourth el_before_av_one_third-faculty'})

specialties = [find_ucla_focus(aoi, 'p') for aoi in area_of_interest]

prof_info = {
    'profName':[link.find('h2').text for link in links],
    'titles':[link.find('p').text for link in links],
    'profLink':[link.find('a', href = True)['href'] for link in links]
}

prof_info['institution'] = 'UCLA'

df = pd.DataFrame.from_dict(prof_info).drop_duplicates()
df['specialties'] = specialties
df.to_sql('professors', engine, if_exists='append', index=False)