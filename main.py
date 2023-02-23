import logging
import os

try:
    fileName = os.curdir + "\\logs\\log.log"
    print(fileName)

    logging.basicConfig(
        filename=fileName,
        level=logging.INFO,
        format="{asctime} {levelname:<8} {message}",
        style="{",
        filemode="a",

    )


except Exception as error:
    logging.info(f"Error occured :{error}")
finally:
    logging.info("Application is shutting down.")
