import pandas as pd
import copy
import uuid


class User:
    def __init__(self, user_id, name, password, currentAuthority):
        self.user_id = user_id
        self.token = ""
        self.name = name
        self.password = password
        self.currentAuthority = currentAuthority

    def set_token(self):
        self.token = str(uuid.uuid4())
        return self.token

    def clean_token(self):
        self.token = None