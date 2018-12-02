import requests
import time
import json
import sys


def request_url(url_str):
    headers = {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
    }
    response = requests.get(url_str, headers=headers)
    json_data = json.loads(response.content)
    subjects_list = json_data['subjects']
    print(subjects_list)
    for subjects in subjects_list:
        print(subjects)
    if 20 > len(subjects_list):
        sys.exit(0)
    time.sleep(3)


def main():
    i = 0
    while True:
        url_str = "https://movie.douban.com/j/search_subjects?type=movie&tag=%%E7%%83%%AD%%E9%%97%%A8&sort=recommend&page_limit=20&page_start=%d" % i
        i += 20
        request_url(url_str)


if __name__ == "__main__":
    main()