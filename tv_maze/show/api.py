import requests


class TvMazeApi:
    def __init__(self):
        self.url_base = 'http://api.tvmaze.com'

    def search_shows(self, search_query):
        url_search_shows = f'{self.url_base}/search/shows?q={search_query}'
        response_api = requests.get(url=url_search_shows)
        return response_api
    
    def get_show_by_id(self, show_id):
        url_get_show = f'{self.url_base}/shows/{show_id}'
        response_api = requests.get(url=url_get_show)
        return response_api
