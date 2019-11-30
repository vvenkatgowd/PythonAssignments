class InvalidCredentials(Exception):
    def __init__(self,msg="Invalid Credentials"):
        Exception.__init__(self,msg)
try:
    names=[
          {
          	"name": "Venkat"
            "password": "849"
          },
          {
          	"name": "Rakesh"
            "password": "656"
          }
          ]
    a=input("Enter username")
    b=input("Enter password")
    userPresent = False
    for i in names:
        if a == i["name"] and b == i["password"]:
            print("Welcome", i["name"], sep=" ")
            userPresent = True
            break
    if not userPresent:
        raise InvalidCredentials("Invalid Credentials")

except InvalidCredentials as e:
    print(e)