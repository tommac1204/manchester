#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import requests
import scraperwiki.sqlite as db

PARENT_ID = 2547# Borough codes



def iter_children_areas_kml(parent_id):
    children = getjs('http://mapit.mysociety.org/area/%s/children' % parent_id)
    for id, data in children.items():
        kml = requests.get('http://mapit.mysociety.org/area/%s.kml' % id).content
        entry = {'parent_area': int(data['parent_area']),
                 'id': int(id),
                 'name': data['name'],
                 'kml': kml}
        yield entry


def getjs(url, **opts):
    return json.loads(requests.get(url, **opts).content)


#
# Main
#
data = list(iter_children_areas_kml(PARENT_ID))
db.save(['id'], data, verbose=0)
# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
