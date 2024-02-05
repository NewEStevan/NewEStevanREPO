# Copyright (C) 2023, NewEStevan.

"""
Example video plugin that is compatible with Kodi 20.x "Nexus" and above
"""
import os
import sys
from urllib.parse import urlencode, parse_qsl

import xbmcgui
import xbmcplugin
from xbmcaddon import Addon
from xbmcvfs import translatePath

# Get the plugin url in plugin:// notation.
URL = sys.argv[0]
# Get a plugin handle as an integer number.
HANDLE = int(sys.argv[1])
# Get addon base path
ADDON_PATH = translatePath(Addon().getAddonInfo('path'))
ICONS_DIR = os.path.join(ADDON_PATH, 'resources', 'images', 'icons')
FANART_DIR = os.path.join(ADDON_PATH, 'resources', 'images', 'fanart')
POSTER_DIR = os.path.join(ADDON_PATH, 'resources', 'images', 'poster')
# Public domain movies are from https://publicdomainmovie.net
# Here we use a hardcoded list of movies simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some website or online service.
VIDEOS = [
    {
        'genre': 'FUTBOL',
        'icon': os.path.join(ICONS_DIR, 'FUTBOL.png'),
        'fanart': os.path.join(FANART_DIR, 'FUTBOL.jpg'),
        'movies': [
            {
                'title': 'M. LaLiga 1080 MultiAudio',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=7d8c87e057be98f00f22e23b23fbf08999e4b02f',
                'poster': os.path.join(POSTER_DIR, 'MLIGA.png'),
            },
            {
                'title': 'M. LaLiga HyperMotion 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=3b50977af3acb17ecd8e463a94888dfbaea028d2',
                'poster': os.path.join(POSTER_DIR, 'LALIGAHYPERMOTION.png'),
            },
            {
                'title': 'DAZN LaLiga 1080 MultiAudio',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=1960a9be8ae9e8c755330218eac4c5805466290a',
                'poster': os.path.join(POSTER_DIR, 'DAZNLALIGA.png'),
            },
            {
                'title': 'DAZN LaLiga 1080 MultiAudio',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=75251ba975132ec9a202806ba5bf606e87280c96',
                'poster': os.path.join(POSTER_DIR, 'DAZNLALIGA.png'),
            },
            {
                'title': 'DAZN 1 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=8ca07071b39185431f8e940ec98d1add9e561639',
                'poster': os.path.join(POSTER_DIR, 'DAZN1.png'),
            },
            {
                'title': 'DAZN 2 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=60dbeeb299ec04bf02bc7426d827547599d3d9fc',
                'poster': os.path.join(POSTER_DIR, 'DAZN2.png'),
            },
            {
                'title': 'DAZN 3 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=a8ffddef56f082d4bb5c0be0d3d2fdd8c16dbd97',
                'poster': os.path.join(POSTER_DIR, 'DAZN3.png'),
            },
            {
                'title': 'DAZN 4 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=2fcdf7a19c0858f686efdfabd3c8c2b92bf6bcfd',
                'poster': os.path.join(POSTER_DIR, 'DAZN4.png'),
            },
            {
                'title': 'M. Deportes 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=d00223931b1854163e24c5c22475015d7d45c112',
                'poster': os.path.join(POSTER_DIR, 'MDEPORTES.png'),
            },
            {
                'title': 'M. Deportes 2 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=e6f06d697f66a8fa606c4d61236c24b0d604d917',
                'poster': os.path.join(POSTER_DIR, 'MDEPORTES.png'),
            },
            {
                'title': 'M.L. Campeones 1080 MultiAudio',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=3a3858cae88f14bbe00f54ba6c9ebf7b1de1e9b6',
                'poster': os.path.join(POSTER_DIR, 'LIGADECAMPEONES.png'),
            },
            {
                'title': 'M.L. Campeones 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=045718bad2ddb4f03b1a420754a97a23ad8b493b',
                'poster': os.path.join(POSTER_DIR, 'LIGADECAMPEONES.png'),
            },
            {
                'title': 'M.L. Campeones 2 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=b373a2d2aa4d1aeb7e0d7fcdbe2ce28edf35bb13',
                'poster': os.path.join(POSTER_DIR, 'LIGADECAMPEONES.png'),
            },
            {
                'title': 'M.L. Campeones 3 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=bb9ec0db8db136f4fcd8986b8681048e2bd95bf1',
                'poster': os.path.join(POSTER_DIR, 'LIGADECAMPEONES.png'),
            },
            {
                'title': 'M.L. Campeones 4 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=297fab10d7364ca1991fa43fcff469573688ce7a',
                'poster': os.path.join(POSTER_DIR, 'LIGADECAMPEONES.png'),
            },  
        ],
    },
    {
        'genre': 'MOTOR',
        'icon': os.path.join(ICONS_DIR, 'MOTOR.png'),
        'fanart': os.path.join(FANART_DIR, 'MOTOR.jpg'),
        'movies': [
            {
                'title': 'DAZN F1 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=5789ca155323664edd293b848606688edf803f4d',
                'poster': os.path.join(POSTER_DIR, 'DAZNF1.png'),
            },
            {
                'title': 'DAZN F1 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=9dad717d99b29a05672166258a77c25b57713dd5',
                'poster': os.path.join(POSTER_DIR, 'DAZNF1.png'),
            },
            {
                'title': 'DAZN F1 720',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=e1fcad9de0c782c157fde6377805c58297ab65c2',
                'poster': os.path.join(POSTER_DIR, 'DAZNF1.png'),
            },
        ],
    },
    {
        'genre': 'OTROS',
        'icon': os.path.join(ICONS_DIR, 'OTROS.png'),
        'fanart': os.path.join(FANART_DIR, 'OTROS.jpg'),
        'movies': [
            {
                'title': 'EuroSport 1 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=5e4cd48c79f991fcbee2de8b9d30c4b16de3b952',
                'poster': os.path.join(POSTER_DIR, 'EUROSPORT1.png'),
            },
            {
                'title': 'EuroSport 2 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=c373da9e901d414b7384e671112e64d5a2310c29',
                'poster': os.path.join(POSTER_DIR, 'EUROSPORT2.png'),
            },
            {
                'title': '#Vamos 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=859bb6295b8d0f224224d3063d9db7cdeca03122',
                'poster': os.path.join(POSTER_DIR, 'MVAMOS.png'),
            },
            {
                'title': 'LaLiga Tv Bar 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=aa82e7d4f03061f2144a2f4be22f2e2210d42280',
                'poster': os.path.join(POSTER_DIR, 'LALIGATVBAR.png'),
            },
            {
                'title': 'M. Golf 1080',
                'url': 'http://127.0.0.1:6878/ace/getstream?id=4f945b0ba4206fa2676b61e9eaa465ac3dcc8122',
                'poster': os.path.join(POSTER_DIR, 'MGOLF.png'),
            },
        ],
    },
]


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :return: plugin call URL
    :rtype: str
    """
    return '{}?{}'.format(URL, urlencode(kwargs))


def get_genres():
    """
    Get the list of video genres

    Here you can insert some code that retrieves
    the list of video sections (in this case movie genres) from some site or API.

    :return: The list of video genres
    :rtype: list
    """
    return VIDEOS


def get_videos(genre_index):
    """
    Get the list of videofiles/streams.

    Here you can insert some code that retrieves
    the list of video streams in the given section from some site or API.

    :param genre_index: genre index
    :type genre_index: int
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[genre_index]


def list_genres():
    """
    Create the list of movie genres in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(HANDLE, 'Public Domain Movies')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(HANDLE, 'movies')
    # Get movie genres
    genres = get_genres()
    # Iterate through genres
    for index, genre_info in enumerate(genres):
        # Create a list item with a text label.
        list_item = xbmcgui.ListItem(label=genre_info['genre'])
        # Set images for the list item.
        list_item.setArt({'icon': genre_info['icon'], 'fanart': genre_info['fanart']})
        # Set additional info for the list item using its InfoTag.
        # InfoTag allows to set various information for an item.
        # For available properties and methods see the following link:
        # https://codedocs.xyz/xbmc/xbmc/classXBMCAddon_1_1xbmc_1_1InfoTagVideo.html
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        info_tag = list_item.getVideoInfoTag()
        info_tag.setMediaType('video')
        info_tag.setTitle(genre_info['genre'])
        info_tag.setGenres([genre_info['genre']])
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&genre_index=0
        url = get_url(action='listing', genre_index=index)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(HANDLE, url, list_item, is_folder)
    # Add sort methods for the virtual folder items
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(HANDLE)


def list_videos(genre_index):
    """
    Create the list of playable videos in the Kodi interface.

    :param genre_index: the index of genre in the list of movie genres
    :type genre_index: int
    """
    genre_info = get_videos(genre_index)
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(HANDLE, genre_info['genre'])
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(HANDLE, 'movies')
    # Get the list of videos in the category.
    videos = genre_info['movies']
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label
        list_item = xbmcgui.ListItem(label=video['title'])
        # Set graphics (poster, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use only poster for simplicity's sake.
        # In a real-life plugin you may need to set multiple image types.
        list_item.setArt({'poster': video['poster']})
        # Set additional info for the list item via InfoTag.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        info_tag = list_item.getVideoInfoTag()
        info_tag.setMediaType('movie')
        info_tag.setTitle(video['title'])
        info_tag.setGenres([genre_info['genre']])
   
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=https%3A%2F%2Fia600702.us.archive.org%2F3%2Fitems%2Firon_mask%2Firon_mask_512kb.mp4
        url = get_url(action='play', video=video['url'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(HANDLE, url, list_item, is_folder)
    # Add sort methods for the virtual folder items
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(HANDLE)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    # offscreen=True means that the list item is not meant for displaying,
    # only to pass info to the Kodi player
    play_item = xbmcgui.ListItem(offscreen=True)
    play_item.setPath(path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(HANDLE, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if not params:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_genres()
    elif params['action'] == 'listing':
        # Display the list of videos in a provided category.
        list_videos(int(params['genre_index']))
    elif params['action'] == 'play':
        # Play a video from a provided URL.
        play_video(params['video'])
    else:
        # If the provided paramstring does not contain a supported action
        # we raise an exception. This helps to catch coding errors,
        # e.g. typos in action names.
        raise ValueError(f'Invalid paramstring: {paramstring}!')


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
