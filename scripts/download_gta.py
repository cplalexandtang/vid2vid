import os
from download_gdrive import *

file_id = '11pjTlcsAnrwMDbDfTei-MZ8gCRx6xxQ3'
chpt_path = './datasets/'
if not os.path.isdir(chpt_path):
	os.makedirs(chpt_path)
destination = os.path.join(chpt_path, 'gtaCity.zip')
download_file_from_google_drive(file_id, destination) 
unzip_file(destination, chpt_path)