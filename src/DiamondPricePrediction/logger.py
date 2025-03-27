import os
import logging
from datetime import datetime

class Log:
    def __init__(self, log_dir='..\logs'):
        # Create log directory path
        self.log_path = os.path.join(os.getcwd(), log_dir)

        # Create the directory if it doesn't exist
        os.makedirs(self.log_path, exist_ok=True)

        print(f"Log directory created at: {self.log_path}")

    def log_file(self):
        # Generate log file name with timestamp
        log_file = f"{datetime.now().strftime('%d-%m-%Y %I-%M-%S-%p')}.log"

        # Create the full log file path
        log_file_path = os.path.join(self.log_path, log_file)

        # Write initial log entry
        # with open(log_file_path, "w") as f:
        #     f.write("Log file created successfully!\n")

        print(f"Log file created at: {log_file_path}")

        # Configure logging
        logging.basicConfig(level=logging.INFO,
                            filename=log_file_path,
                            format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")

        return log_file_path  # Returning log file path in case needed

# Usage
log_instance = Log()
log_instance.log_file()