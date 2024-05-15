
# /utils/config.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010122

import json

class Config:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.config = json.load(file)

    def get_config(self, key):
        return self.config.get(key)

    def set_config(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        with open(config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

# Example usage
if __name__ == "__main__":
    config = Config("config.json")
    print(config.get_config("database_url"))
    config.set_config("database_url", "postgresql://localhost/mydb")
    print(config.get_config("database_url"))
