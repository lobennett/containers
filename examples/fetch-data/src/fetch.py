import os
import requests


def fetch_data():
    # fetch initial screener data
    API_TOKEN = os.getenv("API_TOKEN")
    headers = {"Authorization": f"token {API_TOKEN}", "Cache-Control": "no-cache"}

    with requests.Session() as sess:
        sess.headers.update(headers)

        url = "https://deploy.expfactory.org/api/results/?sc_id=61"
        while url:
            try:
                response = sess.get(url)
                response.raise_for_status()
                data = response.json()
                yield data
                url = data.get("next")
            except requests.RequestException as e:
                print(f"Error fetching data from {url}: {e}")
                yield None
