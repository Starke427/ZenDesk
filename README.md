# ZenDesk
Pull down historical ticket information for auditing and reporting.

## getTickets.py

This script needs to be modified to include your ZenDesk email, API token, and a set number of days you want to look back from today. From there it will query the user API endpoint to get the assignee IDs for your agents and administrators and iterate over those IDs for every day in the given range. This, if piped to an external .csv file, can be imported to excel and delimited based on '|' to provide easily searchable audit records.

## getMetrics.py

This script needs to be modified to include your ZenDesk email, API token, and domain. It will grab metrics on how often a ticket has been opened, reopened, when it was first solved and it's final solve (in minutes).

## getUsers.py

This script needs to be modified to include your ZenDesk email, API token, and domain. It will pull down a full list of users, their assignee ids, and emails.
