import re
from urllib.parse import urljoin

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("chromedriver.exe")

PREFIX="QS"

sno=[]
university_name=[]
country=[]
ranking=[]

count=1

url_list=["https://www.topuniversities.com/university-rankings/world-university-rankings/2020"]

filter_list=["UniversitiesAll", "UniversitiesCanadaCSE", "UniversitiesCanadaGeneralRanking"]

filter=0

next_url=url_list[filter]
# next_url= "https://www.topuniversities.com/university-rankings/world-university-rankings/2020"

base_uri="https://www.usnews.com"

# while next_url != None:
driver.get(next_url)

content=driver.page_source
soup=BeautifulSoup(content,features="html.parser")

for table in soup.findAll('div', attrs={'id':'qs-rankings_wrapper'}):
    if table != None:
        print(table.text)
# for tbody in table.findAll('tbody', attrs={'class':None}):
#     if tbody != None:
#         for row in tbody.findAll('tr', attrs={'role':'row'}):
#             if row != None:
#                 print(row.text)


    # for a in soup.findAll('div', attrs={'class':'sep'}):
    #     name=a.find('h2', attrs={'class':'h-taut'})
    #     if name != None:
    #         sno.append(count)
    #         count += 1
    #         print(name.text)
    #         university_name.append(name.text.strip())
    #         _university_link = name.find('a', attrs={'href': re.compile("^https://")})
    #         if _university_link != None:
    #             sub_driver = webdriver.Chrome("chromedriver.exe")
    #             sub_driver.get(_university_link.get('href'))
    #             sub_content = sub_driver.page_source
    #             sub_soup = BeautifulSoup(sub_content, features="html.parser")
    #             _lint_divs = sub_soup.findAll('div', attrs={'class':'directory-data'})
    #             for l in _lint_divs:
    #                 # print(l)
    #                 _ulink = l.find('a', attrs={'href': re.compile("^https://")})
    #                 if _ulink != None:
    #                     # print(_ulink.get('href'))
    #                     link.append(_ulink.get('href'))
    #                     break
    #                 _ulink = l.find('a', attrs={'href': re.compile("^http://")})
    #                 if _ulink != None:
    #                     # print(_ulink.get('href'))
    #                     link.append(_ulink.get('href'))
    #                     break
    #             sub_driver.close()
    #             # link.append(_university_link.get('href'))
    #
    #     _ranking=a.find('span', attrs={'class':'rankscore-bronze'})
    #     if _ranking != None:
    #         rank=_ranking.text.strip()
    #         if rank.__contains__("Tie"):
    #             rank = rank.split()[0].strip()
    #         ranking.append(rank)
    #
    #     _country_div=a.find('div', attrs={'class':'t-taut'})
    #     if _country_div != None:
    #         _country = _country_div.find('span', attrs={'class': None}).text.strip()
    #         _city_soup = _country_div.find('span', attrs={'class': 't-dim t-small'})
    #         _city=" "
    #         if _city_soup != None and len(_city_soup.text.strip())>0:
    #             _city = _city_soup.text.strip()
    #
    #         country.append(_country)
    #         city.append(_city)
    #         # print(_city)
    #
    # _pager_links = soup.findAll('a', attrs={'class':'pager_link'})
    # if _pager_links != None :
    #     for _link in reversed(_pager_links):
    #         l=str(_link)
    #         if l.__contains__('Next'):
    #             next_url = urljoin(base_uri,_link.get('href'))
    #         else:
    #             next_url=None
    #         break

driver.close()
# print(country)
# df = pd.DataFrame({'SNo.':sno, 'University Name': university_name, 'Country': country, 'City': city, 'International Ranking': ranking, 'Link': link})
# df.to_csv( PREFIX+filter_list[filter]+'.csv', index=False, encoding='ISO-8859-1')