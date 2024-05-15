
# /utils/logging.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010121

import logging

class Logging:
    def __init__(self, log_file):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

# Example usage
if __name__ == "__main__":
    log = Logging("application.log")
    log.log_debug("This is a debug message")
    log.log_info("This is an info message")
    log.log_warning("This is a warning message")
    log.log_error("This is an error message")
