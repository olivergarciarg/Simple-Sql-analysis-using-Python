#Project log analisis

#Description:
loganalysis.py executes 3 queries using the data inthe database that Udacity provided to find the follwing information.
1- What are the 3 most popular articles starting with the most popular
2- Sort the Authors from most popular to least popular
3- Dates with more than 1% error rate when trying to access the webpage

#Environment set up
1- Install Vagrant and the Virtual Machine following the instructions in this URL https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0
2- Download the file newsdata.sql from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
3- save the file newsdata.sql in the folder "Vagrant" of the virtual machine installed in step 1
4- Bring the virtual machine online and log into it
5- cd into vagrant
6- run this command to load the data into the database "psql -d news -f newsdata.sql"
7- copy loganalysis.py into the folder vagrant
8- from the virtual machine run "python loganalysis.py"

#Expected output:
Most popular articles:
Article Candidate is jerk, alleges rival has 342102 views
Article Bears love berries, alleges bear has 256365 views
Article Bad things gone, say good people has 171762 views

Author popularity:
Author Ursula La Multa has 512805 views
Author Rudolf von Treppenwitz has 427781 views
Author Anonymous Contributor has 171762 views
Author Markoff Chaney has 85387 views

Dates with more than 1% error rate:
July 17, 2016 has 2.3% error rate








