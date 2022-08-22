from bs4 import BeautifulSoup
import requests
import json
import re
import os

def get_videos():
    url = "https://www.reddit.com/r/TikTokCringe/top.json"
    response = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
    return response.json()

def get_links(text):
    text = json.loads(json.dumps(text))
    text = str(text)

    pattern = r"https:\/\/v\.redd\.it\/\w{13}"

    links = re.findall(pattern, text)

    reddit_links = []

    for link in links:
        if link not in reddit_links:
            reddit_links.append(link)

    print(reddit_links)

    for link in reddit_links:
        os.system(f'youtube-dl -o "./results/temp/%(title)s.%(ext)s" {link}')

def txt():
    path_of_the_directory = './results/temp/'
    ext = (".mp4")

    with open('./results/temp/videolist.txt', 'w') as f:
        for files in os.listdir(path_of_the_directory):
            if files.endswith(ext):
                f.write(f"file '{files}'\n")
                print(files)
            else:
                continue

def concat(name):
    os.system(f'ffmpeg -f concat -safe 0 -i "./results/temp/videolist.txt" -c copy "./results/final/{name}.mp4"')
    print("Successful video merge")

def delete():
    temp = "./results/temp/"
    for files in os.listdir(temp):
        os.remove(temp+ files)

def make_video():
    name = input("Choose the video name:")
    links = get_videos()
    print(links)
    get_links(links)
    txt()
    concat(name)
    delete()

make_video()