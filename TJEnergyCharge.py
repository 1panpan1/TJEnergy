import requests
from bs4 import BeautifulSoup
from Email import email
from utils import log

def get_energy_value():
    query_url = "http://202.120.163.129:88/default.aspx"
    try:
        data = {
            "__VIEWSTATE": "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",
            "__VIEWSTATEGENERATOR": "CA0B0334",
            "drlouming": 7,
            "drceng": 1275,
            "dr_ceng": 1514,
            "drfangjian": 1812,
            "radio": "usedR",
            "ImageButton1.x": 20,
            "ImageButton1.y": 20
        }
        query_response = requests.post(query_url.strip(), data= data, headers= {"Content-Type":"application/x-www-form-urlencoded"})
    except Exception as e:
        log(str(e))
        return None
    
    if query_response is None:
        log("failed to crawl the query page")
        return None
    else:
        page = query_response.text
    return parse_html(page)

def parse_html(html):
    bs = BeautifulSoup(html, features="html.parser")
    node = bs.find("span", class_="number orange")
    if node is None:
        log("failed to find the energy value in page")
        return None
    else:
        return node.string

if __name__ == "__main__":
    limit = 20.0
    eml = email()
    energy_value = get_energy_value()
    if energy_value is not None:
        energy_value = float(energy_value)
        log("successfully queried the energy value. Energy value is {}".format(energy_value))
        if energy_value > limit: 
            eml_content = {"subject": "622宿舍剩余电费", "content": "622宿舍电费余额{}元".format(energy_value)}
            eml.send_mail(eml_content)
    else:
        log("failed to query the energy value")