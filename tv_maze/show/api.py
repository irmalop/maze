import requests


class TvMazeApi:
    def __init__(self):
        self.url_base = 'http://api.tvmaze.com'

    def search_shows(self, search_query):
        url_search_shows = f'{self.url_base}/search/shows?q={search_query}'
        print(search_query, "search query")
        response_api = requests.get(url=url_search_shows)
        return response_api
    
