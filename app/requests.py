import urllib.request,json

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['API_URL']

def get_quotes():
    quotes_base_url = base_url

    with urllib.request.urlopen(quotes_base_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response:
            quotes_results = get_quotes_response
    
    return quotes_results