import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(filename)s %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Create a console handler and set the level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("[ %(asctime)s ] %(filename)s %(lineno)d %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)
