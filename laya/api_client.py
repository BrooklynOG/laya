import requests

API_URL = "http://127.0.0.1:8000/chat"

def send_query(query):
    try:
        res = requests.post(API_URL, json={"query": query})
        return res.json()["response"]
    except:
        return "Server not running"