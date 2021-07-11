from bs4 import BeautifulSoup
import requests

first_url = "https://stackoverflow.com"
base_url = "https://stackoverflow.com/jobs?r=true&q="

def sof_extract_data(input_result, data_list):
  url = f"{base_url}{input_result}"
  sof_request = requests.get(url)
  sof_soup = BeautifulSoup(sof_request.text, "html.parser")

  result_list = sof_soup.find_all("div", {"class":"js-result"})
  
  for result in result_list:
    data_dict = {}
    title = result.find("h2", {"class":"fc-black-800"}).find("a").string
    company = result.find("h3", {"class":"fc-black-700"}).find("span").string
    link = result.find("h2", {"class":"fc-black-800"}).find("a")["href"]
    link = first_url + link
    
    data_dict["title"] = title
    data_dict["company"] = company
    data_dict["link"] = link
    
    data_list.append(data_dict)

  return data_list

