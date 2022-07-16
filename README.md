# Recruitment-task---backend-internship
Recruitment-task for profil-software.com

# Requirements
Python>=3.10  
pandas==1.4.3  
numpy==1.23.1  

# How use

For running script we need provide path to files with input emails in config/config.json

To run scripts please run script from folder Recruitment-task---backend-internship which contains main.py

To run type in console python main.py -args or python.exe main.py -args

Posible args 

1. Show incorrect emails (--incorrect-emails, -ic)
Print the number of invalid emails, then one invalid email per line.

2. Search emails by text (--search str, -s str) this arg require word for search write for example -s agustin
The Program should take a string argument and print the number of found emails, then one found email per line.

3. Group emails by domain (--group-by-domain, -gbd) 
Group emails by one domain and order domains and emails alphabetically

4. Find emails that are not in the logs file (--find-emails-not-in-logs path_to_logs_file, -f path_to_logs_file) this arg require for proper working for example: -f D:\log_email.log
Find emails that are not in the provided logs file. Print the numbers of found emails, then one found email per line sorted alphabetically.

