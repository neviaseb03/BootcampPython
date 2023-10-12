import re

def hashtags(text):
  
    pattern = r'#\w+'
    hashtags = re.findall(pattern, text)
    return hashtags

social_media_post = input("Enter a sentence")
hashtags = hashtags(social_media_post)
print(hashtags)