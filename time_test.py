from datetime import datetime as d
import time
import requests, json

def safcom_login():
    login_url = 'https://dtsvc.safaricom.com:8480/api/auth/login'
    login_headers = {'X-Requested-With':'XMLHttpRequest','content-type':'application/json'}
    login_data = login_data = {"username": 'Amways_apiuser',"password": 'Admin@123'}

    login_req = requests.post(login_url, headers=login_headers, data = json.dumps(login_data), verify=False)
    
    return login_req.json()

def safcom_tokenRefresh():
    refreshtoken_url = 'https://dtsvc.safaricom.com:8480/api/auth/RefreshToken'
    refreshtoken_headers = {'X-Requested-With':'XMLHttpRequest','content-type':'application/json', 'X-Authorization':'Bearer '+ safcom_login()['refreshToken']}
        
    token_req = requests.get(refreshtoken_url, headers=refreshtoken_headers, verify=False)
    
    return token_req.json()

def safcom_bulksms():
    bulksms_url = 'https://dtsvc.safaricom.com:8480/api/public/CMS/bulksms'
    bulksms_headers = {'X-Authorization':'Bearer '+ safcom_tokenRefresh()['token']}
    bulksms_data = {"timeStamp": str(d.timestamp(d.now())),"dataSet": [ {"userName": 'Amways', "channel": "sms", "packageId": '5115', "oa": 'SDPTest',"msisdn": '254723666748',"message": 'MORNING TO YOU',"uniqueId": 'SD67443222223FJ' }]}

    send_bulksms_req = requests.get(bulksms_url, headers=bulksms_headers, data=json.dumps(bulksms_data), verify=False)
    
    return send_bulksms_req.json()

das=d.strptime('2021-01-28T07:04:10','%Y-%m-%dT%H:%M:%S')

req_url = 'http://139.59.141.223:8000/api/v1/bulksms/sms/'
req_hed = {'content-type':'application/json', 'Authorization':'JWT '+'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMSwidXNlcm5hbWUiOiJSYXNoaWRhIiwiZXhwIjoxNjEyNDA5MTc5LCJlbWFpbCI6InJhc2hpZGFuZ2FuemFsYUBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTYxMTgwNDM3OX0.k8dVoNHlbSxdLnFfTqMqaiyqO5h_o_7marSPW5WyNPI'}

while True:
    time.sleep(1)
    now = d.now()
    if(now.year!= das.year or now.month!= das.month or now.day != das.day or now.hour != das.hour or now.minute != das.minute or now.second != das.second):
        pass
    else:
        safcom_login()
        safcom_tokenRefresh()
        safcom_bulksms()
        print(safcom_bulksms())
        print(now.time())
        break