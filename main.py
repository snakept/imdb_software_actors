import pandas as pd
import requests as req

if __name__ == "__main__":
    actressRequest = req.get(
        "https://imdb-api.com/en/API/IMDbList/k_vhvsnz5j/ls053501318").content
    actressData = pd.read_json(actressRequest)
    actress = actressData['items']
    for actor in actress:
        print(actor['fullTitle'])
