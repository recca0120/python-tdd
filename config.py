import os

import dotenv

dotenv.load_dotenv('.env')

ftp = {
    'host': os.environ.get('FTP_HOST'),
    'username': os.environ.get('FTP_USERNAME'),
    'password': os.environ.get('FTP_PASSWORD'),
}

db = {
    'url': os.environ.get('DB_URL')
}
