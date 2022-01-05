import pip._vendor.requests

response = pip._vendor.requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')


# print json
# print(response.json())


# title data from item
for data in response.json()['items']:
    print(data['title'])