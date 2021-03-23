HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
# if HEROKU:
#     from os import environ
#     API_ID = int(environ["API_ID"])
#     API_HASH = environ["API_HASH"]
#     SUDO_CHAT_ID = int(environ["SUDO_CHAT_ID"])
#     OWNER_ID = int(environ["OWNER_ID"])
#     SESSION_STRING = environ["SESSION_STRING"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 2255574
    API_HASH = "8967d0744d99a1287bbcb837a130cce9"
    SUDO_CHAT_ID =  -1001204473432
    OWNER_ID = 1303091873


# don't make changes below this line
ARQ_API = "https://thearq.tech"
