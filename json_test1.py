import json

str_json = """
{
    "email": "jane@exampleco.com",
    "email_verified": false,
    "username": "janedoe",
    "phone_number": "+199999999999999",
    "phone_verified": false,
    "user_id": "auth0|5457edea1b8f22891a000004",
    "created_at": "",
    "updated_at": "",
    "identities": [
      {
        "connection": "Initial-Connection",
        "user_id": "5457edea1b8f22891a000004",
        "provider": "auth0",
        "isSocial": false
      }
    ],
    "app_metadata": {},
    "user_metadata": {},
    "picture": "",
    "name": "",
    "nickname": "",
    "multifactor": [
      ""
    ],
    "last_ip": "",
    "last_login": "",
    "logins_count": 0,
    "blocked": false,
    "given_name": "",
    "family_name": ""
  }
"""

data = json.loads(str_json)
print(data)
