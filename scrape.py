import requests
from bs4 import BeautifulSoup
from pprint import pprint

p = 1

while True:
    # Scrape Hacker News site
    site = f"https://news.ycombinator.com/?p={p}"
    # print(site)

    try:
        res = requests.get(site)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select(".titleline")
        subtexts = soup.select(".subtext")

        hn = []
        for idx, item in enumerate(links):
            anchor = item.select('a')
            title = anchor[0].getText()
            href = anchor[0].get('href', None)

            score = subtexts[idx].select('.score')
            points = 0
            if len(score):
                points = int(score[0].getText().replace(" points", ""))
            hn.append({
                "title": title, "link": href,
                'votes': points
            })
        hn.sort(key=lambda dict_key: dict_key["votes"], reverse=True)
        pprint(hn)

        scrape_next_page = input("Load more? Y/N: ").upper() == 'Y'
        if scrape_next_page:
            p += 1
            continue
        else:
            print('*** End of program ***')
            break

    except ConnectionError as ce:
        print(f"Failed loading site: {site}\nError: {ce}")
        break
    except Exception as e:
        print(f"Failed loading site: {site}\nError: {e}")
        break

