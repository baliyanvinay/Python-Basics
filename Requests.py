from requests import *
site = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Neha_Sharma_at_Indian_Sports_Honours_Awards_2019_.jpg/800px-Neha_Sharma_at_Indian_Sports_Honours_Awards_2019_.jpg'
site1 = 'https://httpbin.org/post'
payload = {
    'username': 'baliyan',
    'password': 'testing'
}
r = post(site1, data=payload)

print(r.status_code)
print(r.ok)

print(r.json()['form'])
