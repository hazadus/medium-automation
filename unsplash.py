# Download Unsplash Photos
#
# pip install pyunsplash
# https://pyunsplash.readthedocs.io/en/latest/
# https://unsplash.com/oauth/applications
#
from pyunsplash import PyUnsplash
import urllib.request
import api_keys

unsplash = PyUnsplash(api_key=api_keys.API_KEY_UNSPLASH)
images = unsplash.photos(query="Books", count=10, type="random")

for img in images.entries:
    url = img.link_download
    urllib.request.urlretrieve(url, f"{img.id}.jpg")
