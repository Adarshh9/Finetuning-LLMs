import requests

def get_response(query):

    api_key = "sMWzNM6y.qPI4aPmNczofwDkmx2KWX2BcDJDv5gw3"

    headers = {
        'Content-Type' : 'application/json',
        'Apikey' : f'Api-Key {api_key}',
    }

    data = {
        'payload' : query
    }

    url = "https://payload.vextapp.com/hook/BNWQSDBXO6/catch/$(adarshhme)"

    response = requests.post(url ,json=data ,headers=headers)

    return response


query = "What is machine learning?"
response = get_response(query=query)
print(response.text)