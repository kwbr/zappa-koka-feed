from urlparse import urljoin
from flask import Flask, request
from datetime import datetime
from werkzeug.contrib.atom import AtomFeed

import koka

app = Flask(__name__)

def make_external(url):
    if url:
        return urljoin('http://www.koka36.de', url)
    else:
        return None

@app.route("/api/rss/koka")
def koka_feed():

    feed = AtomFeed('Neu im Vorverkauf',
                    feed_url=request.url,
                    url=request.host_url)

    events = koka.get_feed()

    for event in events:
        feed.add(event['title'],
                 unicode(event['description']),
                 content_type='html',
                 url=make_external(event['link']),
                 updated=datetime.utcnow())

    return feed.get_response()

if __name__ == "__main__":
    from os import getuid
    app.debug = (getuid() == 1000)
    app.run()
