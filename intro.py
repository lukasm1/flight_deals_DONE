from requests import post

POST_SHEETS_API = "https://api.sheety.co/76574eaca8ac30a2754a72ed27fe6a9c/flightDeals/users"

print("Welcome to Lukas's Flight Club\nWe find the best flight deals and email you.")
name = input("What is your first name?\n")
surename = input("What is your last name?\n")
while True:
    email = input("What is your email?\n")
    email2 = input("Type your email again.\n")
    if email == email2:
        break

post_params = {
    "user": {
        "firstName": name,
        "lastName": surename,
        "email": email,
    }
}
post_response = post(url=POST_SHEETS_API, json=post_params)

print("You're in the club!")