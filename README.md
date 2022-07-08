# machine_learning_project

start machine learning project

requiremens:-
1. GitHub Account
2. Heroku Account
3. VS Code IDE
4. Git cli


Creating conda environment
'''
conda create -p venv python==3.7 -y
'''
actvate the conda env
'''

or
conda activate venv
'''

'''
pip install -r requirements.txt
'''
To Add files to git
'''
git add
'''

OR
'''
git add <file_name>
'''

Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
'''
git status
'''
To check all version maintained by git
'''
git log
'''

To create version/commit all changes by git 
'''
git commit -m "message"
'''

To send version/changes to github
'''
git push origin main
'''

To check remote url 
'''
git remote -v
'''

To set up CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = chandrunaik456@gmail.com
2. HEROKU_APP_KEY = ff4d29b0-0903-4489-8d3b-9b4826ec0ee3
3. HEROKU_APP_NAME = ml-deplo-app


BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tagname>
> Note - Image name for the docker must be in lowercase
'''

TO list docker image
'''
docker images
'''

TO RUN DOCKER IMAGE
'''
docker run -p 5000:5000 -e PORT = 5000
'''

To check running container in docker
'''
docker ps
'''

To stop an container
'''
docker stop <container_id>

'''

