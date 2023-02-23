import os
import datetime
import sys
from Services.Utils import createTaskFailedStatus
from Services.DataService import DataService

fileExists = os.path.exists("C:\\dev\\projects\\misc\\Tasker\\config.json")
status = createTaskFailedStatus("Test")
DataService.createProcessLog(status)
print(f"Task CheckDonationReceipts.py completed")
