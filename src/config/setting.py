import os

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__)).replace('src/config', "")

settings = {
  "url_database" : f'sqlite:////{os.path.join(PROJECT_PATH, "policies.db")}'
}

# print(settings)