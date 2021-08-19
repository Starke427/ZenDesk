import requests

domain = '' # Zendesk Domain
user = '' + '/token' # Agent email
pwd = '' # Token

def getAgents(user, pwd):
	url = f"https://{domain}.zendesk.com/api/v2/users.json?role[]=agent&role[]=admin"
	response = requests.get(url, auth=(user, pwd))
	if response.status_code != 200:
		print('Status:', response.status_code, 'Problem with the request. Exiting.')
		exit()
	data = response.json()
	userList = data['users']
	for user in userList:
		userId = f"{user['name']}, {user['id']}, MegaplanIT Agent"
		user_list.append(userId)

def getUsers(user, pwd):
	url = f"https://{domain}.zendesk.com/api/v2/users.json?role=end-user"
	userResults = []
	while True:
		user = '' + '/token' # Agent email
		pwd = '' # Token
		response = requests.get(url, auth=(user, pwd))
		if response.status_code != 200:
			print('Status:', response.status_code, 'Problem with the request. Exiting.')
			exit()
		data = response.json()
		userList = data['users']
		for user in userList:
			userId = f"{user['name']}, {user['id']}"
			user_list.append(userId)
		if data['next_page'] == None:
			break
		else:
			url = data['next_page']
			continue

user_list = []
getAgents(user, pwd)
getUsers(user, pwd)
user_list.sort()
for user in user_list:
	print(user)
