import os
import pandas as pd
import pandas as pd
import requests
from bs4 import BeautifulSoup as beautiful
url="https://www.jumia.co.ke/android-phone/"
all_urls=[]
for page in range(10):
    next_urls=url+'?page='+str(page)
    all_urls.append(next_urls)
for url in all_urls:
    render=requests.get(url)
    the_html=beautiful(render.content,'html.parser')
    scrape=the_html.find_all(class_='text-area')
    scraped_data=[]
    for data in scrape:
        scraped_data.append(data.get_text())
        clean_data=[data.replace('\n','') for data in scraped_data]
        clean_data_=[data.replace(' ','') for data in clean_data]
        data_2_csv=pd.DataFrame(clean_data_,columns=['column'])
        data_2_csv.to_csv('jumia-deals',index=False,mode="a")
        print(data_2_csv)
