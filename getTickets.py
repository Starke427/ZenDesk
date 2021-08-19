import requests, datetime, dateutil.parser, sys, time, json
from urllib.parse import urlencode

## Authentication ##
domain = ''
user = '' + '/token' # Agent email
pwd = '' # API Token
daysBack = 90

dates = []
for i in range(0, daysBack):
    date = datetime.date.today()+datetime.timedelta(-i)
    day = f"{date.day:02d}"
    month = f"{date.month:02d}"
    year = f"{date.year:02d}"
    delta = f"{year}-{month}-{day}"
    dates.append(delta)

def getAgents(user, pwd):
	url = f"https://{domain}.zendesk.com/api/v2/users.json?role=agent"
	response = requests.get(url, auth=(user, pwd))
	if response.status_code != 200:
		print('Status:', response.status_code, 'Problem with the request. Exiting.')
		exit()
	data = response.json()

	while url:
		userList = data['users']
		for user in userList:
			userId = f"{user['id']}"
			user_list.append(userId)
		if url == data['next_page']:
			break
		else:
			url = data['next_page']

def getAdmins(user, pwd):
	url = f"https://{domain}.zendesk.com/api/v2/users.json?role=admin"
	response = requests.get(url, auth=(user, pwd))
	if response.status_code != 200:
		print('Status:', response.status_code, 'Problem with the request. Exiting.')
		exit()
	data = response.json()

	while url:
		userList = data['users']
		for user in userList:
			userId = f"{user['id']}"
			user_list.append(userId)
		if url == data['next_page']:
			break
		else:
			url = data['next_page']


user_list = []
getAgents(user, pwd)
getAdmins(user, pwd)

print("TicketID"+"|"+"Created_at"+"|"+"Updated_at"+"|"+"Subject"+"|"+"Status"+"|"+"AssigneeID"+"|"+"Tags"+"|"+"Summary"+"|"+"Category"+"|"+"Priority"+"|"+"NormalizedDate")

for userId in user_list:
    for date in dates:
        url = f"https://{domain}.zendesk.com//api/v2/search.json?query=created%3A{date}+assignee%3A{userId}+type%3Aticket+sort%3Aasc"#.f
        response = requests.get(url, auth=(user, pwd))
        data = response.json()
        for result in data['results']:
            # print(result['url'],'|',end='')
            print(result['id'],'|',end='')
            # print(result['external_id'],'|',end='')
            # print(result['via'],'|',end='')
            print(result['created_at'],'|',end='')
            print(result['updated_at'],'|',end='')
            # print(result['type'],'|',end='')
            print(result['subject'],'|',end='')
            # print(result['raw_subject'],'|',end='')
            # print(result['description'],'|',end='')
            # print(result['priority'],'|',end='')
            print(result['status'],'|',end='')
            # print(result['recipient'],'|',end='')
            # print(result['requester_id'],'|',end='')
            # print(result['submitter_id'],'|',end='')
            print(result['assignee_id'],'|',end='')
            # print(result['organization_id'],'|',end='')
            # print(result['group_id'],'|',end='')
            # print(result['collaborator_ids'],'|',end='')
            # print(result['follower_ids'],'|',end='')
            # print(result['email_cc_ids'],'|',end='')
            # print(result['forum_topic_id'],'|',end='')
            # print(result['problem_id'],'|',end='')
            # print(result['has_incidents'],'|',end='')
            # print(result['is_public'],'|',end='')
            # print(result['due_at'],'|',end='')
            print(result['tags'],'|',end='')
            # print(result['custom_fields'],'|',end='')
            # print(result['satisfaction_rating'],'|',end='')
            # print(result['sharing_agreement_ids'],'|',end='')
            # print(result['fields'],'|',end='')
            # print(result['followup_ids'],'|',end='')
            # print(result['brand_id'],'|',end='')
            # print(result['allow_channelback'],'|',end='')
            # print(result['allow_attachments'],'|',end='')
            # if '|' in result['custom_fields'][7]['value']:
            #     print()
            try:
                stripSummary = result['custom_fields'][7]['value'].replace('\n', '')
                cleanSummary = stripSummary.replace('|', ';')
                print(cleanSummary,'|',end='') # Summary
            except AttributeError:
                print('None','|',end='')
            print(result['custom_fields'][0]['value'],'|',end='')  #Category
            print(result['custom_fields'][1]['value'],'|',end='')  #Priority
            print(" ",((dateutil.parser.parse(result['created_at'])).strftime('%m/%d/%Y')))
        url=data['next_page']
