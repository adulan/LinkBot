# Link Bot

Link Bot is made for Discord and takes social media links and reposts them with a discord embeddable link.

## Discord Permissions

To function fully, Blue Bot requires the ```SERVER MEMBERS INTENT``` and ```MESSAGE CONTENT INTENT``` Priviliged Gateway Intents

It also requires the following Bot Permissions

```Send Mesages```

```Manage Mesages```

```Embed Links```

```Read Messages/View Channels``` (Depreciated?)


## Run Locally

docker build --pull --rm -f "Dockerfile" -t linkbot:latest "."

docker run -it \
--env DISCORD_TOKEN="YOUR_TOKEN" \
--rm --name always_blue.py linkbot:latest

### Environment Variables
| Name | Required | Description |
| --- | --- |--- |
| DISCORD_TOKEN | Required | Discord > Applications > Bot > Token |


## Install from package

```$ docker pull ghcr.io/adulan/linkbot:latest```

Update environment variables in docker-compose.yml

```$ docker compose up -d``` 