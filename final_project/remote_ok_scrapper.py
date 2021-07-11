from bs4 import BeautifulSoup
import requests

first_url = "https://remoteok.io"
base_url = "https://remoteok.io/remote-dev+"
back_url = "-jobs"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def rmok_extract_data(input_result, data_list):
  url = f"{base_url}{input_result}{back_url}"
  rmok_request = requests.get(url, headers=headers)
  rmok_soup = BeautifulSoup(rmok_request.text, "html.parser")
  
  table = rmok_soup.find("table", {"id":"jobsboard"})
  tr_list = table.find_all("tr", {"class":"hot"})
  
  for tr in tr_list:
    data_dict = {}
    title = tr.find("h2", {"itemprop":"title"}).string
    company = tr.find("h3", {"itemprop":"name"}).string
    link = first_url + tr["data-url"] 


    data_dict["title"] = title
    data_dict["company"] = company
    data_dict["link"] = link
    
    data_list.append(data_dict)

  return data_list