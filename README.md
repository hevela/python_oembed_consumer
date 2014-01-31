Python Oembed Consumer
======================

This module uses Python-oembed (https://github.com/abarmat/python-oembed) to provide a simple consumer wich supports several Oembed providers.

Currently the following sites are supported:
* Youtube (http://www.youtube.com/)
* Flickr (http://www.flickr.com/)
* Qik (http://qik.com/)
* Revision 3 (http://revision3.com/)
* Hulu (http://www.hulu.com/)
* Vimeo (https://vimeo.com/)
* College Humor (http://www.collegehumor.com/)
* Poll Everywhere (http://www.polleverywhere.com/)
* I Fix It (http://www.ifixit.com/)
* SmugMug (http://www.smugmug.com/)
* Slide Share (http://www.slideshare.net/)
* 23 HQ (http://www.23hq.com/)
* 5min (http://www.5min.com)
* Twitter (http://www.twitter.com)
* Photobucket (http://www.photobucket.com)
* Daily Motion (http://www.dailymotion.com)
* Click Through (http://new.clikthrough.com/)
* Dot Sub (http://dotsub.com/)
* Blip (http://blip.tv/)
* VHX (http://VHX.tv/)
* National Film Board of Canada (http://www.nfb.ca/)
* Instagram (http://instagram.com)
* Wordpress TV (http://wordpress.tv/)
* SoundCloud (http://soundcloud.com/)
* Screenr (http://www.screenr.com/)

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
    
