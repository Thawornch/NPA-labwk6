import http.client
import json

url = "api.football-data.org"
token = "0e970a96ee4b4074a11f187448c20951"

"""
BL1 : Bundesliga
PL : Premier Leauge
SA : Serie A
PD : Spain Primera Division
FL1: France Ligue 1
WC : World Cup
CL : Champions-League
"""
num = 1

while True:
    leauge = input("Choose Leauge: ")
    if leauge == "end":
        break
    connection = http.client.HTTPConnection(url)
    print("URL: " + (url))
    print("="*128)
    headers = { 'X-Auth-Token': token }
    connection.request('GET', '/v2/competitions/'+leauge+'/scorers', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    
    for event in response["scorers"]:
        player_name = event["player"]["name"]
        goals_number = event["numberOfGoals"]
        team = event["team"]["name"]
        print("%d. %s\tgoals: %d\tclub: %s" % (num, player_name, goals_number, team))
        num += 1
    num = 1
    print("="*128)
