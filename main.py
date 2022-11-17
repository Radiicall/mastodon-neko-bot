# Mastodon Bot
from mastodon import Mastodon
import time
import nekos
import requests

while True:
    if time.strftime("%-H") == "12":
        image_url = nekos.img("neko")

        r = requests.get(image_url) # create HTTP response object

        with open("neko.png",'wb') as f:
            f.write(r.content)

        mastodon = Mastodon(
            access_token = 'pytooter_usercred.secret',
            api_base_url = 'https://mastodon.social'
        )

        mastodon.status_post(status=None, in_reply_to_id=None, media_ids=mastodon.media_post("neko.png", "image/png"), sensitive=False, visibility=None, spoiler_text=None, language=None, idempotency_key=None, content_type=None, scheduled_at=None, poll=None, quote_id=None)
    print(time.strftime("%-H"))
    time.sleep(900)
