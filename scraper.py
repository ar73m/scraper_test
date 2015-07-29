# -*- coding: utf-8 -*-
import scraperwiki
import lxml.html

print("Get HTML")
html = scraperwiki.scrape("http://lenta.ru/")

root = lxml.html.fromstring(html)
a = root.xpath('.//div[@class="items"]//div[@class="item"]')

for r in a:
    date = r.xpath('./time/@datetime')[0]
    text = r.xpath('./a/text()')[0]
    url =  r.xpath('./a/@href')[0]
    
    print("{} -- {}".format(date.encode('utf-8'), text.encode('utf-8')))
    print("http://lenta.ru{}".format(url.encode('utf-8')))
    
    scraperwiki.sqlite.save(
    unique_keys=[],
    data={"time": date,
          "text": text,
          "url": u"http://lenta.ru{}".format(url)
        })
        
        
        
# .encode('cp866') decode('cp1251')




# # Write out to the sqlite database using scraperwiki library
#scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
#scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".