import glob
import json
import logging
import os
from TaskRunner import TaskRunner

try:
    logging.info("Application started.")

    fileName = os.curdir + "\\logs\\log.log"
    logging.basicConfig(
        filename=fileName,
        level=logging.INFO,
        format="{asctime} {levelname:<8} {message}",
        style="{",
        filemode="a",
    )

    config_file = open("config.json")
    config = json.load(config_file)
    scriptDir = config["scriptDir"]
    files = glob.glob(f"{scriptDir}\\*.py")

    print("running task runner")
    taskRunner = TaskRunner.executeTask(files)

except Exception as error:
    logging.info(f"Error occured :{error}")
finally:
    logging.info("Application is shutting down.")
