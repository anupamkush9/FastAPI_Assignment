# For Runnig the Project at your local

### Install virtualenv
> sudo apt install python3-virtualenv

<br>

### Create Virtual Environment by below command
> virtualenv venv

<br>

### Activate virtualenv
> source virtualenv/bin/activate

<br>

### Install All Requirements
> pip install -r requirements.txt

<br>

### Define All env_template Variables with their correct values in .env file
* Variable names are defined in env-template file

<br>

### Command For Running project
> uvicorn main:app --reload

<br>

### For viewing swagger below visit  
* http://127.0.0.1:8000/docs#/
