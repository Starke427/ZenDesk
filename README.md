# ZenDesk
Pull down historical ticket information for auditing and reporting.

## getTickets.py

This script needs to be modified to include your ZenDesk email, API token, and a set numbe of days you want to look back from today. From there it will query the user API endpoint to get the assignee IDs for your agents and administrators and iterate over those IDs for every day in the given range. This, if piped to an external .csv file, can be imported to excel and delimited based on '|' to provide easily searchable audit records.
