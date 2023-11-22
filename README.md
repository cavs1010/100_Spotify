# 🎵 Billboard Hot 100 Spotify Playlist Creator
[Introduction](#introduction_h) | [Functionality](#functionality_h) | [Technologies](#technologies_h) | [Setup and Usage](#setup_usage_h) | [Acknowledgements](#acknowledge_h) | [License](#license_h)

<p>Create Spotify playlists based on Billboard Hot 100 charts for any given date.</p><br>

<h2>Introduction<a name="introduction_h"></a></h2>
<p>This project aims to automate the creation of Spotify playlists based on Billboard's Hot 100 chart for a specified date. It is designed for music enthusiasts who want to revisit popular music from a specific time period. The script fetches song data from the Billboard Hot 100 and then searches for these tracks on Spotify, creating a nostalgic playlist for the user.</p><br>

<h2>Functionality<a name="functionality_h"></a></h2>
<p>The program works by first asking the user for a target date. It then scrapes the Billboard Hot 100 chart for that date to get the list of top songs. Using Spotify's API, it searches for these songs and creates a new Spotify playlist, adding the found tracks to this playlist. The script also handles various edge cases and errors, such as invalid date formats and missing songs on Spotify.</p><br>

<h2>Technologies<a name="technologies_h"></a></h2>
<p></p>
<a href="https://www.python.org"><img src='https://raw.githubusercontent.com/get-icon/geticon/master/icons/python.svg' width="40" height="40" alt='python'/></a>
<a href="https://www.crummy.com/software/BeautifulSoup/"><img src='images/beatiful_soup.png' width="70" height="40" alt='BeautifulSoup'/></a>
<a href="https://developer.spotify.com/documentation/web-api/"><img src='images/spotify.png' width="65" height="45" alt='Spotify API'/></a>
<a href="https://requests.readthedocs.io/en/master/"><img src='images/requests.jpg' width="50" height="50" alt='Requests'/></a>
<p></p><br>

<h2>Setup and Usage<a name="setup_usage_h"></a></h2>
<p>To use this script, you need to have Python installed on your machine along with the BeautifulSoup, Spotipy, and Requests libraries. You also need to set up a Spotify Developer account and create an app to obtain your client ID and client secret. These credentials should be set as environment variables. Detailed instructions on setup and usage can be found in the accompanying documentation.</p><br>

<h2>Acknowledgements<a name="acknowledge_h"></a></h2>
<p>Special thanks to the Billboard for maintaining an extensive database of music charts and to Spotify for providing an accessible API for music data and playlist management.</p>

<h2>License<a name="license_h"></a></h2>
<p>Licensed under MIT License.</p>
