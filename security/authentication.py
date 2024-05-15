
# /security/authentication.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010120

import hashlib

class Authentication:
    def __init__(self):
        self.users = {}

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = self.hash_password(password)

    def authenticate_user(self, username, password):
        if username in self.users and self.users[username] == self.hash_password(password):
            return True
        return False

# Example usage
if __name__ == "__main__":
    auth = Authentication()
    auth.register_user("user1", "securepassword")
    print(auth.authenticate_user("user1", "securepassword"))  # Output: True
    print(auth.authenticate_user("user1", "wrongpassword"))   # Output: False
