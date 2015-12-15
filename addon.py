from xbmcswift2 import Plugin, xbmcgui
from resources.lib import latenightlive

plugin = Plugin()

URL = "http://abc.net.au/radionational/programs/latenightlive"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('latest_podcasts'),
            'thumbnail': "http://a2.mzstatic.com/us/r30/Music4/v4/45/ff/6e/45ff6eb2-18c8-5aa4-e365-bf429a117f4a/cover170x170.jpeg"}, 
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('browse_subjects'),
            'thumbnail': "http://www.abc.net.au/radionational/image/5698480-3x2-700x467.jpg"},
    ]

    return items


@plugin.route('/latest_podcasts/')
def latest_podcasts():
    """
    contains playable podcasts listed as latest podcasts
    """
    items = latenightlive.get_audio()
    
    return items


@plugin.route('/browse_subjects/')
def browse_subjects():
    """
    contains a list of navigable podcast by subjects
    """
    items = []

    soup = abcradionational.get_soup(URL + "/")
    
    subject_heading = abcradionational.get_podcast_heading(soup)
    
    for subject in subject_heading:
        items.append({
            'label': subject['title'],
            'path': plugin.url_for('subject_item', url=subject['url']),
        })

    return items



if __name__ == '__main__':
    plugin.run()
