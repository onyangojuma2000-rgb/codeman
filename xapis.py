 #parse a real X API
# This is what the X API v2 returns when you fetch a post
# Structure: data (the post) + includes (the author details
x_response = {
    "data": {
        "id": "2076589716036608320",
        "text": "Live by a code:\n\n* Loyalty.\n* Strength.\n* Honour.\n* Discipline.\n\nIf you stand for nothing, you fall for anything.",
        "created_at": "2026-07-14T05:30:00Z",
        "author_id": "748352990",
        "public_metrics": {
            "retweet_count": 2104,
            "reply_count":    487,
            "like_count":   11380,
            "quote_count":    319,
            "bookmark_count": 4251
        }
    },
    "includes": {
        "users": [
            {
                "id": "748352990",
                "name": "Amerix",
                "username": "amerix",
                "public_metrics": {
                    "followers_count": 1200000,
                    "following_count": 487
                }
            }
        ]
    }
}

# Parse it exactly as you have been parsing all lesson
post    = x_response["data"]
author  = x_response["includes"]["users"][0]
metrics = post["public_metrics"]
likes = metrics["like_count"]
retweets = metrics["retweet_count"]
replies = metrics["reply_count"]
followers = author["public_metrics"]["followers_count"]
pct_engagement_rate = (likes + replies + retweets) / followers * 100
print("POST")
print(f"  Author:    @{author['username']} ({author['name']})")
print(f"  Text:      {post['text'][:60]}...")
print(f"  Posted:    {post['created_at']}")
print()
print("ENGAGEMENT")
print(f"  Likes:     {metrics['like_count']:,}")
print(f"  Retweets:  {metrics['retweet_count']:,}")
print(f"  Replies:   {metrics['reply_count']:,}")
print(f"  Bookmarks: {metrics['bookmark_count']:,}")
print()
print(f"Engagement Rate: {round(pct_engagement_rate, 2)}%")
print(f"AUTHOR: @{author['username']} has {author['public_metrics']['followers_count']:,} followers")
print(f"Read more at: https://x.com/{author['username']}")
