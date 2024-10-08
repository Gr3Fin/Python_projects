# 100 songs playlist in Spotify

> Creates a playlist in Spotify for the desired moment in time, by scraping the billboard.com webpage.
---
**Skills and Tools Covered:**
- API
- Environmental variables
- List comprehension
- Web page scraping with BeautifullSoap
---
**NOTE**:  
 1. Spotify account is needed.  
 2. Create a Spotify App (https://developer.spotify.com/dashboard/) to get ClientID and Client Secret - for API authorization.  
 3. Spotify uses OAuth to allow third-party applications to access a Spotify user's account without giving them the username or password.  
 4. Use _http://example.com_ as your Redirect URI (make sure you set the redirect URI in the Spotify Dashboard as well).  
 5. To make it work you have to create a token.txt file (if Billboar is connected to Spotify)
---
**NOTE:**
* 100_songs.py - _create a playlist by typing the desired date._
* Used Spotify API
---
Useful links:  
- [Billboard hot 100](https://www.billboard.com/charts/hot-100/)
- [Spotify](https://open.spotify.com/)
- [Spotify API doc](https://developer.spotify.com/documentation/web-api)
- [OAuth documentation](https://spotipy.readthedocs.io/en/2.13.0/#spotipy.oauth2.SpotifyOAuth)
- [spotipy](https://spotipy.readthedocs.io/en/2.13.0/#)
