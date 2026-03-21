from instabot import Bot
bot=Bot()


# login kro bot ko real username aur password se

bot.login(username="any username",password="password ")

bot.follow("username uska jisse is id se follow krna ho ")

bot.upload_photo("path of photo")


bot.unfollow("username of userid jisko unfollow krna ho ")

bot.send_message("write something",["username1","username2"])

followers=bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(follower))