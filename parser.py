import re
from BeautifulSoup import BeautifulSoup

# The Applications.html file you want to parse
htmlFile = './applications/apps-1-28-11.html'

# Applicant
# [City, State]
# Application ID
# Contact
# [Phone]
# [Email]
# Project title
# Program
# Proposed Project Area 
# Funding type
# Funding Round
# Grant Request
# Loan Request
# Status
# Grant Award
# Loan Award
# Description
# Executive Summary
# Public Notice Response [PDF]

html = open(htmlFile, 'r')

soup = BeautifulSoup(html.read())
html.close()

# soup = BeautifulSoup(file('test_apps.html').read())

apps = soup.findAll("tbody")

output = ['Applicant', 'City', 'State', 'Application ID', 'Contact Name', 'Contact phone', 'Contact email', 'Project Title', 'Program', 'Project area', 'Project type', 'Funding Round', 'Grant request', 'Loan Request', 'Status', 'Grant Award', 'Loan Award', 'Description', 'Executive Summary', 'Tribes Served', 'Public Notice Response', 'Fact Sheet']
print '\t'.join(output)

for app in apps:
	 
	if (not(app.table) and app.find(text="Applicant") ): # Bunch of BS so we get the right tbody with no inner tables
	
		# start
		line = app.find('b')
	
		# Applicant
		applicant = app.find(text="Applicant").parent.parent.nextSibling.string
				
		# City & State
		_locale = app.find(text="Applicant").parent.parent.parent.nextSibling.nextSibling
		_locale = _locale.find('td').nextSibling.string
		_locale = _locale.split(", ")
		city = _locale[0]
		state = _locale[1]
	 	
	 	# Application ID
	 	application_id = app.find(text="Application ID").parent.parent.nextSibling.string
	 	
	 	# Contact Info
	 	contact_name = app.find(text="Contact").parent.parent.nextSibling.string
		
		try:
			contact_phone = app.find(text="Contact").parent.parent.parent.nextSibling.nextSibling(text=True)
			contact_phone = contact_phone[0]
		except:
			contact_phone = '-'
		
		try: 
			contact_email = app.find(text="Contact").parent.parent.parent.nextSibling.nextSibling.nextSibling.nextSibling(text=True)
			contact_email = contact_email[0]
		except:
			contact_email = '-'
		
		# Project title
		project_title = app.find(text="Project&nbsp;title").parent.parent.nextSibling.string
		if project_title == None: # using HTML in the text. Boo!!!!!
			project_title = app.find(text="Project&nbsp;title").parent.parent.nextSibling(text=True)
			project_title = ''.join(project_title)
	
	
		# Program
		program = app.find(text="Program").parent.parent.nextSibling.string
		
		# Proposed Project Area
		project_area = app.find(text="Proposed Project Area").parent.parent.nextSibling.string
		
		# Project Type
		project_type = app.find(text="Project type").parent.parent.nextSibling.string
	
		# Funding Round
		try:
			funding_round = app.find(text="Funding Round").parent.parent.nextSibling.string
		except:
			funding_round = '-'
	
		# Grant request
		try: 
			grant_request = app.find(text="Grant&nbsp;request").parent.parent.nextSibling.string
		except:
			grant_request = '-'
			
		# Loan Request
		try:
			loan_request = app.find(text="Loan&nbsp;request").parent.parent.nextSibling.string
		except:
			loan_request = '-'
		
		# Status
		status = app.find(text="Status").parent.parent.nextSibling.string
	
		# Grant award
		try: 
			grant_award = app.find(text="Grant Award").parent.parent.nextSibling.string
		except:
			grant_award = '-'
			
		# Loan award
		try: 
			loan_award = app.find(text="Loan Award").parent.parent.nextSibling.string
		except:
			loan_award = '-'
			
		# Description
		description = app.find(text="Description").parent.parent.nextSibling.string

		if description == None: # using HTML in the description. Boo!!!!!
			description = app.find(text="Description").parent.parent.nextSibling(text=True)
			description = ''.join(description)
			
		# Executive Summary URL
		try:
			executive_summary_url = app.find(text="Executive Summary").parent.parent.nextSibling.find('a')
			executive_summary_url = executive_summary_url['href']
		except:
			executive_summary_url = '-'
			
		# Tribes Served URL
		try:
			tribes_served_url = app.find(text="Tribes Served").parent.parent.nextSibling.find('a')
			tribes_served_url = executive_summary_url['href']
		except:
			tribes_served_url = '-'
			
		# Public Notice Response URL
		try:
			public_notice_response_url = app.find(text="Public Notice Response").parent.parent.nextSibling.find('a')
			public_notice_response_url = public_notice_response_url['href']
		except:
			public_notice_response_url = '-'	
			
		# Fact Sheet URL
		try:
			fact_sheet_url = app.find(text="Fact Sheet").parent.parent.nextSibling.find('a')
			fact_sheet_url = fact_sheet_url['href']
		except:
			fact_sheet_url = '-'	
	
		output = [applicant, city, state, application_id, contact_name, contact_phone, contact_email, project_title, program, project_area, project_type, funding_round, grant_request, loan_request, status, grant_award, loan_award, description, executive_summary_url, tribes_served_url, public_notice_response_url, fact_sheet_url]
		try:
			output = '\t'.join(output)
			print output.encode('ascii', 'replace') #ignore weird characters, we can trust BeautifulSoup, but apparently not the terminal
		except:
			print applicant
				

# 	rows = app.findAll('tr')
# 	for row in rows:
# 		sub_data = []
# 		
# 		col = row.findAll('td')
# 		if len(col) > 1: 	
# 			if col[1].find('a'):
# 				link = col[1].find('a')
# 				data = link['href']
# 			else :
# 				data = col[1].string
# 			
# 			if col[0].string :
# 				
# 				
# 				
# 	
# 	
# 	#applicant = app.find('b').find(text="Applicant").parent.parent.nextSibling.string
# 

# 	rows = app.findAll('tr',)
# 	for row in rows:
# 		title = row.findAll('td')
# 
# 		print title.findAll(text=True)
	 

# f = open('extract.txt', 'w')
# f.write()
# f.close()