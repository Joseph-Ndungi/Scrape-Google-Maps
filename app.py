from outscraper import ApiClient


api_cliet = ApiClient(api_key='KEY_FROM_OUTSCRAPER')
response = api_cliet.google_maps_search(
    'Restaurants near Los Angeles, USA',
    language='en',
    region='es',
    limit=100
)