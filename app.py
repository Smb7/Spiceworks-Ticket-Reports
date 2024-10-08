import csv
from datetime import datetime, timedelta
import pprint
import pandas as pd 

print("Spice Works Report")
printVar = """
Select an option:
1. Get number of tickets assigned to administrator
2. Get Tickets completed 
3. See 30 days trends based on type of ticket
4. Shane statstics  
5. Exit
"""
print(printVar)

# CSV file: 10/4/2024
filename = "All_Tickets.csv"

fields = []
rows = []

def getNumberofTickets():

    fields = []
    rows = []

    get_DateInput = int(input("Enter date to search: "))

    assignee_shane = "Shane Brennan"
    assignee_matt = "Matt Robinson"
    assignee_kyle = "Kyle Martin"
    today = datetime.now()
    last_month = today - timedelta(days=get_DateInput)

    with open(filename, 'r') as csvfile:
        
        csvreader = csv.reader(csvfile)
        
        fields = next(csvreader)

        assignee_idx = fields.index("assignee")
        date_idx = fields.index("created")

        shane_tickets = 0
        matt_tickets = 0
        kyle_tickets = 0

        for row in csvreader:
            assignee = row[assignee_idx]
            ticket_date = row[date_idx]

            try:
                ticket_date = datetime.strptime(ticket_date, '%b %d, %Y @ %I:%M %p')
            except ValueError:
                continue

            if assignee == assignee_shane and ticket_date >= last_month:
                shane_tickets += 1
                rows.append(row)
            
            elif assignee == assignee_matt and ticket_date >= last_month:
                matt_tickets += 1
                rows.append(row)

            elif assignee == assignee_kyle and ticket_date >= last_month:
                kyle_tickets += 1
                rows.append(row)
        
        print(f"Total number of tickets assigned to {assignee_shane} in the 30 days: {shane_tickets}")
        print(f"Total number of tickets assigned to {assignee_matt} in the 30 days: {matt_tickets}")
        print(f"Total number of tickets assigned to {assignee_kyle} in the 30 days: {kyle_tickets}")

# create a function that gets all the response time and close time 
def getResponseTime():
    df = pd.read_csv('All_Tickets.csv')
    
    sort_order = df.sort_values(by=['assignee'])

    print(sort_order)

# this is for user input and choice 
userchoice = int(input("Enter selection: "))
choice = 0 
while choice == 0:
    if userchoice == 1: # shows tickets per admin 
        choice += 1
        getNumberofTickets()
    elif userchoice == 2: # tickets completed shane
        choice += 1
        print
    elif userchoice == 3: # shows trends 
        choice += 1
        print
    elif userchoice == 4: # prints my statstics 
        getResponseTime()
    elif userchoice == 5:
        print("Good bye...")
    else:
        print("Unknow error try again. ")
        userchoice = int(input("Enter selection: "))