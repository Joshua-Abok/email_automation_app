# Email Automation App

## STEPS TO RUN THE PROJECT 

### Tech Stack 
* **Language:** Python 3.11+
* **Libraries:** `python-dotenv`

## Getting started 

### Installation 
1. get to clone the repository

```
git clone https://github.com/Joshua-Abok/email_automation_app.git
cd email_automation_app      # changing directory to the folder
```
2. Create and activate the virtual environment

```
python -m venv .venv
.venv\Scripts\activavate    # for Windows 
# source .venv/bin/activate   # Linux or macos
```
3. install necessary packages
bash 
```
pip install -r requirements.txt
```

### Configuration 
- create .env file in the root directory and add the following keys. 
- Reference file `.env.sample`

```
SENDER_EMAIL='input sender mail'
EMAIL_AUTO_PASS='input sender password'
RECEIVER_EMAIL='input receiver'
```

## Usage 
- how to run the file 
```
python main.py
```