from tweet_harvester import app
from os import environ
# port = os.environ['PORT']
# 'app' originates from the line 'app = Flask(__name__)'
app.run(port=environ.get("PORT", 8080))