# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor
from .vimeo import VHXEmbedIE


class LesMillsOnDemandIE(InfoExtractor):
    _VALID_URL = r'https?://watch\.lesmillsondemand\.com/(?:[^/]+/)*?videos/(?P<id>[^/?#&]+)'
    _TESTS = [{
        'url': 'https://watch.lesmillsondemand.com/videos/bodypump-111-55-min',
        'only_matching': True,
    }, {
        'url': 'https://watch.lesmillsondemand.com/bodypump/season:1/videos/bodypump-111-55-min',
        'only_matching': True,
    }]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        embed_url = self._search_regex(r'<script[^>]*>[^<]*\bembed_url\s*:\s*"([^"]*)"', webpage, 'embed_url')

        return {
            '_type': 'url_transparent',
            'url': VHXEmbedIE._smuggle_referrer(embed_url, url),
            'ie_key': VHXEmbedIE.ie_key(),
            'id': video_id,
            'title': self._og_search_title(webpage),
            'description': self._html_search_meta('description', webpage),
        }
