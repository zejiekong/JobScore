# JobScore
A prototype to filter relevant jobs according to job seekers' needs and profile, JobScore matches the resume content with job listed online, and generates scoring system for suggested job list to make better decision

## Key Features
1. Rank job results according to suitability with user's profile and needs
2. Automatically populates users' information by extracting information from resume

## Tech Stack Used
- Flask: web application

# Setup
On Linux/MacOS, run
``` 
pip install virtualenv
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
FLASK_APP=jobscore.py
flask run
```

On Windows, run
```
pip install virtualenv
virtualenv venv
source venv\scripts\activate
pip install -r requirements.txt
FLASK_APP=jobscore.py
flask run
```