#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a
    given subreddit. Returns 0 if an invalid subreddit is given.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'MyRedditAPIClient/1.0 (by u/yourusername)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    
    except requests.RequestException:
        return 0
