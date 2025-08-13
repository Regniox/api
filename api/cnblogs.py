from flask import Blueprint, request, jsonify
import feedparser

cnblogs_bp = Blueprint('cnblogs', __name__)

@cnblogs_bp.route('/cnblogs_posts/')
def cnblogs_posts():
    u = request.args.get('u')
    # default get blogs quantity = 3
    quantity = request.args.get('quantity', 3, type = int)
    feed_url = "https://feed.cnblogs.com/blog/u/" + u + "/rss/"
    feeds = []
    try:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            if quantity == 0:
                break
            feeds.append({
                'title': entry.title,
                'published': entry.published,
                'link': entry.link,
                'summary': entry.summary

            })
            quantity -= 1
        return feeds
    except:
        return jsonify({'error': 'Failed to parse feed'}), 500
