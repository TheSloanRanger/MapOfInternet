import requests

scraped_urls = set()


def scrape(
    url,
    depth_limit,
    depth=0,
):

    print(f"Scraping {url} at depth {depth}")

    scraped_urls.add(url)

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}. Error: {e}")
        return

    if response.status_code != 200:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return

    text = response.text.split(">")

    for line in text:
        if 'href="https' in line or 'HREF="https' in line:
            if 'href="https' in line:
                position = line.find('href="https')
            else:
                position = line.find('HREF="https')

            string = ""
            for i in range(position + 6, len(line)):
                if line[i] == '"':
                    break
                string += line[i]

            new_url = (
                url.replace("/", "-")
                .replace(":", "=")
                .replace("?", "")
                .replace("&", "and")
            )

            output_path = f"/home/ben/Code/MapOfInternet/Websites/{new_url}.md"
            with open(output_path, "a", encoding="utf-8") as out:
                out.write(f"[[{string.replace('/', '-')}]]\n")

            if string not in scraped_urls and depth < depth_limit:
                scrape(string, depth_limit, depth + 1)

    print("FINISHED SCRAPING: ", url)


def main():

    while True:
        print("Welcome to the Map of Internet program.")
        print()
        print(
            "This program uses a list of the most popular websites, and scrapes them recursively to create a map of the internet. Or you can enter a single origin website to recursively scrape from."
        )
        print()
        print("1) Scrape from a list of popular websites")
        print("2) Scrape from a single origin website")
        print()
        choice = input("Please enter your choice (1 or 2): ")

        if choice not in ("1", "2"):
            print("Invalid choice.")
            # clear the console
            print(chr(27) + "[2J")
            continue

        if choice == "1":
            list_scrape()

        if choice == "2":
            single_scrape()


def list_scrape():
    depth = input(
        "How many levels deep would you like to scrape? (default 1, max 100): "
    )

    if not depth:
        depth = 1

    with open("urls.txt", "r", encoding="utf-8") as url_list:
        for url in url_list:
            url = url.strip()
            scrape(f"https://www.{url}", depth_limit=int(depth))


def single_scrape():
    url = input("Please enter the URL to scrape (include https://): ")
    if not url or "https://" not in url:
        print("Invalid URL.")
        return

    depth = input(
        "How many levels deep would you like to scrape? (default 1, max 100): "
    )

    if not depth:
        depth = 1

    scrape(url, depth_limit=int(depth))


if __name__ == "__main__":
    main()
