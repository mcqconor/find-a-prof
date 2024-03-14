import pandas as pd
from bs4 import BeautifulSoup
from helper_functions import get_soup, clean_ou_names
import sqlalchemy

engine_string = 'mysql+mysqlconnector://root:password@localhost:3306/professorswork'
engine = sqlalchemy.create_engine(engine_string, echo=True)

soup1 = get_soup('https://history.fas.harvard.edu/faculty_alpha')
soup2 = get_soup('https://history.fas.harvard.edu/faculty_alpha?page=2')
soup3 = get_soup('https://history.fas.harvard.edu/faculty_alpha?page=3')

results = [soup1, soup2, soup3]

merged_results = []
for rs in results:
    merged_results.extend(rs)

soup = BeautifulSoup(''.join(map(str, merged_results)), 'html.parser')

name_divs = soup.find_all(lambda tag: tag.name == 'h1' and tag.get('class') == ['node-title'])
content_divs = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['field-item even'])

print(content_divs)

prof_info = {
    'profName':[nd.find('a').text for nd in name_divs],
    'profLink':[nd.find('a', href=True)['href'] for nd in name_divs]
}

# print(prof_info)

prof_info['titles'] = ''
prof_info['institution'] = 'Harvard University'
# df=pd.DataFrame.from_dict(prof_info)
# df.to_sql('professors', engine, if_exists='append', index=False)