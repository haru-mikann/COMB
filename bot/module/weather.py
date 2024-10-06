import requests
def weather(place):
    tokyo = requests.get("https://weather.tsukumijima.net/api/forecast/city/130010").json()
    aichi = requests.get("https://weather.tsukumijima.net/api/forecast/city/230010").json()

    # response = [tokyo["forecasts"][0]["date"].replace("-","/"),tokyo["forecasts"][0]["telop"]]

    response_tokyo = [tokyo["forecasts"][0]["date"].replace("-","/"),tokyo["forecasts"][0]["telop"]]
    response_aichi = [aichi["forecasts"][0]["date"].replace("-","/"),aichi["forecasts"][0]["telop"]]
    
    if place == "aichi":
        return (f"{response_aichi[0]}\n愛知の天気は{response_aichi[1]}")
    
    elif place == "tokyo":
        return (f"{response_tokyo[0]}\n東京の天気は{response_tokyo[1]}")
    
    else:
        return ("未実装")
    