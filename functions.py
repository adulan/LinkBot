# Functions
async def replace_message(message, new_msg):
    try:
        await message.channel.send(new_msg)
        await message.delete()
    except Exception as e:
        print("Error sending message")
        print(e)

async def replace_instagam_link(message):
    content = message.content
    new_msg = content.replace("://www.instagram.com", "://www.ddinstagram.com")
    new_msg = new_msg.replace("://instagram.com", "://www.ddinstagram.com")
    author = message.author.display_name
    new_msg = f"{author} posted a link to Instagram: {new_msg}"
    await replace_message(message, new_msg)

async def replace_tiktok_link(message):
    content = message.content
    new_msg = content.replace("://www.tiktok.com", "://www.vxtiktok.com")
    new_msg = new_msg.replace("://tiktok.com", "://www.vxtiktok.com")
    author = message.author.display_name
    new_msg = f"{author} posted a link to TikTok: {new_msg}"
    await replace_message(message, new_msg)

async def replace_twitter_link(message):
    content = message.content
    new_msg = content.replace("://www.twitter.com", "://www.fxtwitter.com")
    new_msg = new_msg.replace("://twitter.com", "://www.fxtwitter.com")
    new_msg = new_msg.replace("://www.x.com", "://www.fxtwitter.com")
    new_msg = new_msg.replace("://x.com", "://www.fxtwitter.com")
    author = message.author.display_name
    new_msg = f"{author} posted a link to Twitter: {new_msg}"
    await replace_message(message, new_msg)