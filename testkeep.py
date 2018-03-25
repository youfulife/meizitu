import requests
import json

headers = {
    "Host": "api.gotokeep.com",
    "Cookie": "authorization=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1NzA3ZGVkN2NkN2ZjYzE0MDVkN2EwMTgiLCJ1c2VybmFtZSI6IuiwnOS4gOagt-eahOiDoeahg-WkueWtkCIsImF2YXRhciI6IiIsImdlbmRlciI6Ik0iLCJkZXZpY2VJZCI6IjRiMjI3ZjkzMTEwYjQ4YWU4OGVmMDJiNjJhMDE4ODRjZmUwZDQxZjQiLCJpc3MiOiJodHRwOi8vd3d3LmdvdG9rZWVwLmNvbS8iLCJleHAiOjE1MzA0NDIxNTgsImlhdCI6MTUyMTgwMjE1OH0.e6sufQ_7sFFinFKNpsVnx2cmroCqMpbPpCR1Gu69tHA; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%225707ded7cd7fcc1405d7a018%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; x-channel=Apple%20Store; x-device-id=4b227f93110b48ae88ef02b62a01884cfe0d41f4; x-is-new-device=false; x-keep-timezone=Asia%2FShanghai; x-locale=zh-Hans-CN; x-manufacturer=Apple; x-model=iPhone%208; x-model-raw=iPhone10%2C1; x-os=iOS; x-os-version=11.2; x-request-id=a8f150564c931c9ea2d12e5ecfae822b; x-screen-height=667; x-screen-width=375; x-user-id=5707ded7cd7fcc1405d7a018; x-version-code=11722; x-version-name=5.8.0",
    "User-Agent": "Keep/5.8.0 (iPhone; iOS 11.2; Scale/2.00)",
    "x-timestamp": "1521808717957",
    "x-bundleId": "com.gotokeep.keep",
    "x-device-id": "4b227f93110b48ae88ef02b62a01884cfe0d41f4",

    "Connection": "keep-alive",
    "x-version-code": "11722",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1NzA3ZGVkN2NkN2ZjYzE0MDVkN2EwMTgiLCJ1c2VybmFtZSI6IuiwnOS4gOagt-eahOiDoeahg-WkueWtkCIsImF2YXRhciI6IiIsImdlbmRlciI6Ik0iLCJkZXZpY2VJZCI6IjRiMjI3ZjkzMTEwYjQ4YWU4OGVmMDJiNjJhMDE4ODRjZmUwZDQxZjQiLCJpc3MiOiJodHRwOi8vd3d3LmdvdG9rZWVwLmNvbS8iLCJleHAiOjE1MzA0NDIxNTgsImlhdCI6MTUyMTgwMjE1OH0.e6sufQ_7sFFinFKNpsVnx2cmroCqMpbPpCR1Gu69tHA",
    "Accept-Language": "zh-Hans-CN;q=1",
    "x-user-id": "5707ded7cd7fcc1405d7a018",
    "Accept": "*/*",
    "Accept-Encoding": "br, gzip, deflate",
}

url = 'https://api.gotokeep.com/social/v3/timeline/hot'
r = requests.get(url, verify=False)
entries = filter(lambda x: x['author']['gender'] is not 'M', json.loads(r.text)['data']['entries'])
images = []
for entry in entries:
    images += entry["images"]
    images.append(entry['photo'])

for image in images:
    print(image)
