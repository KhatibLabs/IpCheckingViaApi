import requests
import json
choice = int(input("1-for a single ip \n2-for 4 ips \nchoice: "))
if choice == 2:
    Ips = []
    for i in range(4):
        ip_add = input('Enter Ip address : ')
        Ips.append(ip_add)
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    for i in range(4):
        print('>>>>>>>>>>Results for : ' + Ips[i] + '<<<<<<<<<<')
        params = {'apikey': 'YourApiKey', 'ip': Ips[i]}
        response = requests.get(url, params=params)
        print(json.dumps(response.json(), sort_keys=True, indent=2))
        if i == i:
            print('**********************************************************************************')
    print('+++++++++++++++++++++++++++++++++++++++Ipabuse ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    for g in range(4):
        print('>>>>>>>>>>Results for : ' + Ips[g] + '<<<<<<<<<<')
        url = 'https://api.abuseipdb.com/api/v2/check'
        querystring = {
            'ipAddress': Ips[g],
            'maxAgeInDays': '30'
        }
        headers = {
            'Accept': 'application/json',
            'Key': 'Your Api KEY'
        }
        response = requests.request(method='GET', url=url, headers=headers, params=querystring)
        decodedResponse = json.loads(response.text)
        print(json.dumps(decodedResponse, sort_keys=True, indent=4))
        print('***********************************************************************************')









elif choice == 1:
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    ip_add = input("Enter an ip address: ")
    print('>>>>>>>>>>Results for : ' + ip_add + '<<<<<<<<<<')
    params = {'apikey': 'Your Api KEY', 'ip': ip_add}
    response = requests.get(url, params=params)
    print(json.dumps(response.json(), sort_keys=True, indent=2))
    print('**********************************************************************************')
    print('+++++++++++++++++++++++++++++++++++++++Ipabuse ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        'ipAddress': ip_add,
        'maxAgeInDays': '30'
    }

    headers = {
        'Accept': 'application/json',
        'Key': 'Your Api KEY'
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    # Formatted output
    decodedResponse = json.loads(response.text)
    print('>>>>>>>>>>Results for : ' + ip_add + '<<<<<<<<<<')
    print(json.dumps(decodedResponse, sort_keys=True, indent=4))


else:
    print('option not found')












    


