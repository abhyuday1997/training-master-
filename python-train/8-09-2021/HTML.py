import requests
from bs4 import BeautifulSoup as Soup
import pandas as pd


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}


url = 'https://www.cricbuzz.com/live-cricket-scorecard/32058/4th-test-india-tour-of-england-2021'
requests.get(url)
page = requests.get(url)

soup = Soup(page.text, "html.parser")
Inning1 = soup.find_all('div',id="innings_1")[0]
Inning1_batting = Inning1.find_all('div',class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[0]
Inning1_bowling = Inning1.find_all('div',class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[1]
Inning1_batting = Inning1_batting.find_all('div',class_="cb-col cb-col-100 cb-scrd-itms")
Inning1_bowling = Inning1_bowling.find_all('div',class_="cb-col cb-col-100 cb-scrd-itms ")
print(type(Inning1_batting))
Inning1_batting_info = []

for b in Inning1_batting:
# pprint(b)
    batsman = {}
    name = b.find('a',class_="cb-text-link")
    if name:
      pid = name['href'][10:]
      batsman['pid'] = str(pid[:pid.find('/')])
      batsman['name'] = str(name.get_text()).strip()
      if '(' in batsman['name']:
        batsman['name'] = batsman['name'][:batsman['name'].find('(')].strip()
    out_by = b.find('span',class_="text-gray")
    if out_by:
      batsman['out_by'] = str(out_by.get_text()).strip()
    runs = b.find('div',class_="cb-col cb-col-8 text-right text-bold")
    if runs:
      batsman['runs'] = str(runs.get_text()).strip()
    all_others = b.find_all('div',class_="cb-col cb-col-8 text-right")
    if len(all_others)>0:
      batsman['balls'] = str(all_others[0].get_text()).strip()
      batsman['fours'] = str(all_others[1].get_text()).strip()
      batsman['sixes'] = str(all_others[2].get_text()).strip()
      batsman['sr'] = str(all_others[3].get_text()).strip()
    # print all_other
    if len(batsman) > 0:
         Inning1_batting_info.append(batsman)

dat = pd.DataFrame( Inning1_batting_info)
print('Indian Batsman_Name')
print(list(dat['name']))
select = str(input("Select Batsman:"))
print(dat[dat['name']==select])
