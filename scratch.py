import requests                 #Get content
import csv
from bs4 import BeautifulSoup   #Web scraping
import re                       #Regular Expression
import sys                      #For argument parsing

#file = open('url.csv')




if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error:Please enter the TED talk URL")

url = 'https://www.ted.com/talks/sir_ken_robinson_do_schools_kill_creativity'


r = requests.get(url)
print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")
for val in soup.findAll("script"):
    if(re.search("__NEXT_DATA__", str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+.mp4)",result).group("url")
mp4_url = result_mp4.split('"')[0]
print("Downloading the video from..." + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in ...."+ file_name)

r = requests.get(mp4_url)

with open(file_name,'wb') as f:
    f.write(r.content)

print("Download Process finished.")

