from urllib2 import urlopen, URLError
from urlparse import urlsplit

import oembed

__author__ = 'velocidad'

SHORT_URL_DOMAINS = [
    'tinyurl.com',
    'goo.gl',
    'bit.ly',
    't.co',
    'youtu.be',
    'vbly.us',
]

REGEX_PROVIDERS = [
    {
        u'hostname': ('www.youtube.com',),
        u'regex': [
            'regex:.*youtube\.com/watch.*',
            'regex:.*youtube\.com/playlist.*'
        ],
        u'endpoint':'http://www.youtube.com/oembed',
    },
    {
        u'hostname': ('www.flickr.com',),
        u'regex': ['http://*.flickr.com/*'],
        u'endpoint':'http://www.flickr.com/services/oembed',
    },
    {
        u'hostname': ('qik.com',),
        u'regex': ['http://qik.com/video/*', 'http://qik.com/*'],
        u'endpoint':'http://qik.com/api/oembed.%s',
    },
    {
        u'hostname': ('revision3.com',),
        u'regex': ['http://*revision3.com/*'],
        u'endpoint':'http://revision3.com/api/oembed/',
    },
    {
        u'hostname': ('www.hulu.com',),
        u'regex': ['http://www.hulu.com/watch/*'],
        u'endpoint':'http://www.hulu.com/api/oembed.%s',
    },
    {
        u'hostname': ('vimeo.com',),
        u'regex': ['http://vimeo.com/*', 'https://vimeo.com/*'],
        u'endpoint':'http://vimeo.com/api/oembed.%s',
    },
    {
        u'hostname': ('www.collegehumor.com',),
        u'regex': ['http://www.collegehumor.com/video/*'],
        u'endpoint':'http://www.collegehumor.com/oembed.%s',
    },
    {
        u'hostname': ('www.polleverywhere.com',),
        u'regex': ['http://www.polleverywhere.com/polls/*',
                   'http://www.polleverywhere.com/multiple_choice_polls/*',
                   'http://www.polleverywhere.com/free_text_polls/*'],
        u'endpoint':'http://www.polleverywhere.com/services/oembed/',
    },
    {
        u'hostname': ('www.ifixit.com',),
        u'regex': ['http://www.ifixit.com/*'],
        u'endpoint':'http://www.ifixit.com/Embed',
    },
    {
        u'hostname': ('smugmug.com', 'www.smugmug.com'),
        u'regex': ['http://*.smugmug.com/*'],
        u'endpoint':'http://api.smugmug.com/services/oembed/',
    },
    {
        u'hostname': ('www.slideshare.net', 'fr.slideshare.net'),
        u'regex': ['http://www.slideshare.net/*/*'],
        u'endpoint':'http://www.slideshare.net/api/oembed/2',
    },
    {
        u'hostname': ('www.23hq.com',),
        u'regex': ['http://www.23hq.com/*/photo/*'],
        u'endpoint':'http://www.23hq.com/23/oembed',
    },
    {
        u'hostname': ('www.5min.com',),
        u'regex': ['http://www.5min.com/Video/*'],
        u'endpoint':'http://api.5min.com/oembed.%s',
    },
    {
        u'hostname': ('twitter.com',),
        u'regex': ['https://twitter.com/*/status*/*'],
        u'endpoint':'https://api.twitter.com/1/statuses/oembed.%s',
    },
    {
        u'hostname': ('photobucket.com', 'img.photobucket.com'),
        #http://pic.pbsrc.com/dev_help/Metadata/Metadata_Discovery.htm
        u'regex': ['regex:.*photobucket\\.com/(albums|groups)/.+$'],
        u'endpoint':'http://photobucket.com/oembed',
    },
    {
        u'hostname': ('www.dailymotion.com',),
        #http://www.dailymotion.com/doc/api/oembed.html
        u'regex': ['http://www.dailymotion.com/video/*'],
        u'endpoint':'http://www.dailymotion.com/services/oembed',
    },
    {
        u'hostname': ('clikthrough.com', 'www.clikthrough.com'),
        u'regex': ['http://*.clikthrough.com/theater/video/*'],
        u'endpoint':'http://clikthrough.com/services/oembed',
    },
    {
        u'hostname': ('dotsub.com',),
        #http://solutions.dotsub.com/oEmbed
        u'regex': ['http://dotsub.com/view/*'],
        u'endpoint':'http://dotsub.com/services/oembed',
    },
    {
        u'hostname': ('blip.tv',),
        # blit.tv sends an invalid mime-type back
        u'regex': ['http://*blip.tv/*'],
        u'endpoint':'http://blip.tv/oembed/',
    },
    {
        u'hostname': ('official.fm',),
        #http://official.fm/developers/oembed
        u'regex': [
            'http://official.fm/tracks/*',
            'http://official.fm/playlists/*'
        ],
        u'endpoint':'http://official.fm/services/oembed.%s',
    },
    {
        u'hostname': ('vhx.tv',),
        #http://dev.vhx.tv/oembed.html
        u'regex': ['http://vhx.tv/*'],
        u'endpoint':'http://vhx.tv/services/oembed.%s',
    },
    {
        u'hostname': ('www.nfb.ca',),
        u'regex': ['http://*.nfb.ca/film/*'],
        u'endpoint':'http://www.nfb.ca/remote/services/oembed/',
    },
    {
        u'hostname': ('instagr.am', 'instagram.com'),
        #http://instagr.am/developer/embedding/
        u'regex': ['http://instagr.am/p/*', 'http://instagr.am/p/*',
                   'http://instagram.com/p/'],
        u'endpoint': 'http://api.instagram.com/oembed',
    },
    {
        u'hostname': ('wordpress.tv',),
        u'regex': ['http://wordpress.tv/*'],
        u'endpoint': 'http://wordpress.tv/oembed/',
    },
    {
        u'hostname': ('soundcloud.com', 'snd.sc'),
        u'regex': [
            'http://soundcloud.com/*', 'http://soundcloud.com/*/*',
            'http://soundcloud.com/*/sets/*', 'http://soundcloud.com/groups/*',
            'http://snd.sc/*', 'https://soundcloud.com/*'
        ],
        u'endpoint': 'http://soundcloud.com/oembed',
    },
    {
        u'hostname': ('www.screenr.com',),
        #http://blog.screenr.com/post/2145539209/screenr-now-supports-oembed
        u'regex': ['http://www.screenr.com/*', 'http://screenr.com/*'],
        u'endpoint': 'http://www.screenr.com/api/oembed.%s',
    },
]


class Consumer():
    def __init__(self, req_format="json"):
        self.format = req_format
        self.consumer = oembed.OEmbedConsumer()
        self.init_endpoints(self.consumer, self.format)

    def get_oembed(self, url):
        url = self.unshort_url(url)
        response = self.consumer.embed(url)
        return response.getData()

    @staticmethod
    def init_endpoints(selfconsumer, req_format):
        for provider in REGEX_PROVIDERS:
            try:
                endpoint_url = provider[u'endpoint'] % req_format
            except TypeError:
                endpoint_url = provider[u'endpoint']

            endpoint = oembed.OEmbedEndpoint(
                endpoint_url,
                provider[u'regex'])
            selfconsumer.addEndpoint(endpoint)

    @staticmethod
    def unshort_url(geturl):
        host = urlsplit(geturl)[1]

        if host in SHORT_URL_DOMAINS:
            try:
                response = urlopen(geturl, )
                return response.url
            except URLError:
                pass

        return geturl

if __name__ == "__main__":
    consumer = Consumer(req_format="json")
    test_urls = [
        'https://www.youtube.com/watch?v=KdWUZ_49-Ck',
        'https://www.youtube.com/watch?v=V_ho5Y-Yw8g',
        'http://www.flickr.com/photos/hsf6525/12222676506/in/explore-2014-01-30',
        'http://www.flickr.com/photos/hsf6525/11859492884/in/photostream/',
        'http://instagram.com/p/jztoJ7hoRM/',
        'http://instagram.com/p/j2E_SloqDA/',
        'http://www.dailymotion.com/video/x1amn6h_mega-resena-mega-man-10_videogames',
        'http://www.dailymotion.com/video/x1a92ug_video-resena-robocop-arcadia-nes-pc_videogames',
        'https://twitter.com/Kotaku/status/429336310625869824',
        'https://twitter.com/PlayStation/status/429336310856560640',
        'https://soundcloud.com/devolverdigital/sets/hotline-miami-official'
    ]
    for url in test_urls:
        print "\n________________________________"
        print url
        print "\n________________________________"
        embed = consumer.get_oembed(url)
        print embed, "\n\n=================================\n\n"
