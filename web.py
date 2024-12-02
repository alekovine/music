import cloudscraper
import nltk
import random
import tenacity
import time
nltk.data.path.append("/home/vm/.cache/nltk_data")


scraper = cloudscraper.create_scraper()


def random_word():
    return random.choice(nltk.corpus.words.words())


def random_number(a=0, b=10):
    return random.randint(a, b)


def random_agent():
    return f"{random_word()} {random_number()}.{random_number()}.{random_number()}"


def random_email():
    return f"{random_word()}@{random_word()}.com"


def random_requst_header():
    return {"User-Agent": random_agent(), "From": random_email()}


def web_request(url):
    return scraper.get(url, headers=random_requst_header())


def web_status(response):
    return response.status_code == 200


@tenacity.retry(wait=tenacity.wait.wait_exponential(multiplier=1, min=4, max=256))
def web_safe(url, sleep=2):
    response = web_request(url)
    time.sleep(sleep)
    if not web_status(response):
        raise Exception()
    return response

def web_unsafe(url, sleep=2):
    response = web_request(url)
    time.sleep(sleep)
    if not web_status(response):
        raise Exception()
    return response


if __name__ == "__main__":
    nltk.download("words", download_dir="/home/vm/.cache/nltk_data")
