from bs4 import BeautifulSoup
import requests

first_url = "https://weworkremotely.com"
base_url = "https://weworkremotely.com/remote-jobs/search?term="

def wewr_extract_data(input_result, data_list):
  url = f"{base_url}{input_result}"
  wewr_request = requests.get(url)
  wewr_soup = BeautifulSoup(wewr_request.text, "html.parser")

  li_list = wewr_soup.find("section", {"id":"category-2"}).find_all("li", {"class":"feature"})
  
  for li in li_list:
    data_dict = {}
    title = li.find("span", {"class":"title"}).string
    company = li.find("span", {"class":"company"}).string
    link = first_url + li.find("a")["href"]

    data_dict["title"] = title
    data_dict["company"] = company
    data_dict["link"] = link
    
    data_list.append(data_dict)

  return data_list
    