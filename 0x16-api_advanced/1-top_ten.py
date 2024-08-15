#!/usr/bin/python3
"""Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""

import requests

def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Debug: Check the status code
        print("Status Code:", response.status_code)
        
        # Debug: Print the response content to see what is returned
        print("Response Content:", response.content)
        
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            
            # Print titles of the first 10 posts
            for i in range(min(10, len(children))):
                print(children[i].get('data', {}).get('title'))
        else:
            print("None")
    except (requests.RequestException, ValueError) as e:
        print(f"Error: {e}")
        print("None")
