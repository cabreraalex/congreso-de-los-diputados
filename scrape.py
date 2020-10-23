import requests
from bs4 import BeautifulSoup

x = 55
while x > 0:
    url = 'http://www.congreso.es/portal/page/portal/Congreso/PopUpCGI?CMD=VERLST&BASE=pu14&FMT=PUWTXDTS.fmt&DOCS=1-1&QUERY=(DSCD-14-PL-' + \
        str(x) + '.CODI.)'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', class_='texto_completo')
    header = soup.find_all('div', class_='subtitular_texto')
    title = '-'.join(header[0].get_text().split(' ')[-5:])
    with open('./2019/' + title + '.txt', 'w') as f:
        print(results[0].get_text(), file=f)
    x -= 1
