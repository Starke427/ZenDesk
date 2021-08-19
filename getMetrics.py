import requests, datetime
from urllib.parse import urlencode


date = datetime.date.today() + datetime.timedelta(-90)
day = f"{date.day:02d}" # Added for 90 day
month = f"{date.month:02d}"
year = f"{date.year:02d}"
params = {
    'query': 'created>{}-{}-{} type:ticket'.format(year,month,day),
    'sort_by': 'created_at',
    'sort_order': 'asc'        # from oldest to newest
}
domain = '' # ZenDesk domain
url = f"https://{domain}.zendesk.com/api/v2/ticket_metrics.json?" + urlencode(params)
user = '' + '/token' # Agent email
pwd = '' # Token

print("ticket_id"+";"+"created_at"+";"+"updated_at"+";"+"reopens"+";"+"replies"+";"+"first_resolution_time_in_minutes"+";"+"full_resolution_time_in_minutes")
while url:
    response = requests.get(url, auth=(user, pwd))
#    if response.status_code != 200:
#        print('Status:', response.status_code, 'Problem with the request. Exiting.')
#        exit()
    data = response.json()
    ticket_metrics_list = data['ticket_metrics']
    for ticket_metrics in ticket_metrics_list:
        print(" ",ticket_metrics['ticket_id'],';',end='')
        print(" ",ticket_metrics['created_at'],';',end='')
        print(" ",ticket_metrics['updated_at'],';',end='')
        print(" ",ticket_metrics['reopens'],';',end='')
        print(" ",ticket_metrics['replies'],';',end='')
        print(" ",ticket_metrics['first_resolution_time_in_minutes']['calendar'],';',end='')
        print(" ",ticket_metrics['full_resolution_time_in_minutes']['calendar'],';')
        url=data['next_page']
