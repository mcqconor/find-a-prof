import pandas as pd
from helper_functions import get_soup, clean_ou_names, get_links
import sqlalchemy

engine_string = 'mysql+mysqlconnector://root:password@localhost:3306/professorswork'
engine = sqlalchemy.create_engine(engine_string, echo=True)

soup = get_soup('https://history.princeton.edu/people/faculty')


name_divs = soup.find_all({'span':{'class':'field field--name-title field--type-string field--label-hidden'}})
content_divs = soup.find_all(class_ = 'field--name-field-ps-people-title.field--type-string.field--label-hidden.field__item')

class_name = 'field--name-field-ps-people-title field--type-string field--label-hidden field__item'

print(content_divs)

prof_info = {
    'profName':[clean_ou_names(nd, 'a') for nd in name_divs],
    'profLink':[get_links(nd,'a', prefix='https://history.princeton.edu') for nd in name_divs],
    'titles':[clean_ou_names(cd,'a') for cd in content_divs]
}

prof_info['profName'] = [item for item in prof_info['profName'] if item != '']
prof_info['profLink'] = [item for item in prof_info['profLink'] if item != '']
prof_info['titles'] = [item for item in prof_info['titles'] if item != '']

# print(prof_info)
# print(prof_info)

prof_info['titles'] = ''
prof_info['institution'] = 'Harvard University'
# df=pd.DataFrame.from_dict(prof_info)
# df.to_sql('professors', engine, if_exists='append', index=False)