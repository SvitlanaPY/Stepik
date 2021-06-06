import json

str_json = """
{
  "response": {
    "count": 5961777,
    "users": [
      {
        "userId": "krish",
        "jobTitle": "Developer",
        "firstName": "\u041a\u0420\u0406\u0428",
        "lastName": "Lee",
        "region": "CA",
        "phoneNumber": "123456",
        "emailAddress": "krish.lee@learningcontainer.com",
        "likes": 233,
        "userAge": 18,
        "date_now": "04.06.21",
        "canAccess": true,
        "Null_None": null
      },
      {
        "userId": "devid",
        "jobTitle": "Developer",
        "firstName": "Devid",
        "lastName": "Rome",
        "region": "CA",
        "phoneNumber": "1111111",
        "emailAddress": "devid.rome@learningcontainer.com",
        "likes": 234,
        "userAge": 43,
        "date_now": "04.06.21",
        "canAccess": true,
        "Null_None": null
      },
      {
        "userId": "tin",
        "jobTitle": "Program Manager",
        "firstName": "tin",
        "lastName": "jonson",
        "region": "CA",
        "phoneNumber": "2222222",
        "emailAddress": "tin.jonson@learningcontainer.com",
        "likes": 157,
        "userAge": 27,
        "date_now": "04.06.21",
        "canAccess": true,
        "Null_None": null
      }
    ]
  }
}

"""

data = json.loads(str_json)
print(data)
