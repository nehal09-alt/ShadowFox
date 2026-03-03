import requests 
from bs4 import BeautifulSoup
import time 
import re    #regular expression module 

url = "https://old.reddit.com/r/worldnews/"
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; NehalScraper/1.0; learning-purpose)"
}

output_file = "WorldNews.txt"

def all_data(text):
    if not text:
        return ""
    text = text.strip()
    text = re.sub(r"\s+", " ",text)
    return text
def scraping_data(url):
    r = requests.get(url,headers = headers)
    if r.status_code !=200:
        print("Blocked :" , r.status_code)
        return[]
    soup = BeautifulSoup(r.text , "html.parser")
    posts = soup.select("div.thing")

    data = []

    for post in posts :
        title_space = post.select_one("a.title")
        author_space = post.select_one("a.author")
        score_space  = post.select_one("div.score")


        title = all_data(title_space.text)if title_space else "N/A"
        author = all_data(author_space.text) if author_space else "N/A"
        upvotes = score_space.get("title" , "O" ) if score_space else "O"

        link = title_space['href'] if title_space else ""
        if link.startswith("/"):
            link = "https://old.reddit.com" + link


        data.append({
            "Title" : title,
            "Author" : author , 
            "UpVotes" : upvotes , 
            "Link" : link
        })
    return data 
def save_to_txt_file(data,filename):
    with open (filename, "w" ,encoding = "utf-8") as f :
               for post in data :
                    f.write("=" * 40 + "\n")
                    f.write(f"Title   :  {post['Title']} \n")
                    f.write(f"Author  :  {post['Author']} \n")
                    f.write(f"UpVotes :  {post['UpVotes']} \n")
                    f.write(f"Link    :  {post['Link']} \n")
                    f.write("=" *40 + "\n\n")
    print(f"Your File Save as {filename}")

if __name__ == "__main__":
     
     print("Scraping WORLD NEWS ......")
     posts = scraping_data(url)
     time.sleep(3)
     save_to_txt_file(posts , output_file)
     print(f"All Work Done Please Check........WorldNews.txt")