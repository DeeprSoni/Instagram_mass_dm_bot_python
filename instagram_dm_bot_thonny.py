from time import sleep
from instabot import Bot

my_bot = Bot()

user_name = "onlygiveawayshere"
#user_name = str(input("Enter the username to get their followers: "))


#login

my_bot.login(user_name="onlygiveawaysmessage", password="ds06bb01")



followers_id = my_bot.get_user_followers(user_name)

print(followers_id)
'''for count, each_follower in enumerate(followers_id):
    if count > 10:
        break
    my_bot.follow(each_follower)
    sleep(7)

    username = my_bot.get_username_from_user_id(each_follower)
    message = "Hello "+ username +", \n Want to grow your account quickly? \n We have an easy solution. \n We host giveaways with a celebrity @paola_mayfield  with over 1 Million followers! \n Join us in the giveaway to gain tons of followers in a short duration and grow your account. \n Price: $399 USD (negotiable) \n Offer: Invite 2 more people to this giveaway and get 50% discount, or invite a total of 3 people and enter this giveaway for FREE and a GUARENTEED spot for our next giveaway. \n Limited spots left.\n Reply if interested, open to doubts and negotiations."

    my_bot.send_message(message, [username])
    sleep(30)'''

my_bot.logout()