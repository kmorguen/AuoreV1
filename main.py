import requests
from bs4 import BeautifulSoup


url = 'https://www.amazon.com/Intel-i9-10850K-Desktop-Processor-Unlocked/dp/B08DHRG2X9/ref=sr_1_19?dchild=1&fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=74069509-93ef-4a3c-8dca-a9e3fa773a64&pf_rd_r=YHNQX08B3DG19BK95NFX&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1487012920&rnid=16225007011&s=computers-intl-ship&sr=1-19'

headers =  {"User-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'}

page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id = "productTitle").get_text()

print(title.strip())