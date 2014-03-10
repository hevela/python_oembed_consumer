Python Oembed Consumer
======================

This module uses Python-oembed (https://github.com/abarmat/python-oembed) to provide a simple consumer wich supports several Oembed providers.

Currently the following sites are supported:

* app.net - link
* wordpress.com - link
* deviantart.com - photo
* geo-en.hlipp.de - photo
* geograph.org.gg - photo
* geograph.org.uk - photo
* gmep.org - photo
* instagr.am - photo
* smugmug.com - photo
* www.23hq.com - photo
* www.flickr.com - photo
* www.mobypicture.com - photo
* ifttt.com - rich
* cacoo.com - rich
* chirb.it - rich
* crowdranking.com - rich
* huffduffer.com - rich
* meetup.com - rich
* official.fm - rich
* rdio.com - rich
* roomshare.jp - rich
* shoudio.com - rich
* sketchfab.com - rich
* soundcloud.com - rich
* speakerdeck.com - rich
* twitter.com - rich
* www.circuitlab.com - rich
* www.dailymile.com - rich
* www.dipity.com - rich
* www.ifixit.com - rich
* www.kickstarter.com - rich
* www.mixcloud.com - rich
* www.polleverywhere.com - rich
* www.slideshare.net - rich
* animoto.com - video
* aol.com - video
* blip.tv - video
* dotsub.com - video
* justin.tv - video
* revision3.com - video
* sapo.pt - video
* ted.com - video
* ustream.tv - video
* vimeo.com - video
* wordpress.tv - video
* www.collegehumor.com - video
* www.dailymotion.com - video
* www.funnyordie.com - video
* www.hulu.com - video
* www.jest.com - video
* www.nfb.ca - video
* www.screenr.com - video
* www.viddler.com - video
* www.videojug.com - video
* www.youtube.com - video
* yandex.ru - video


Installation
------------

This module requires python-oembed:

    pip install python-oembed
    
Then simply download or clone this repo and import the module:

    from python_oembed_consumer import Consumer
    
    consumer = Consumer()
    url = 'https://soundcloud.com/devolverdigital/sets/hotline-miami-official'
    #This returns a dict with the oembed data
    embed = consumer.get_oembed(url)
    print embed
    
