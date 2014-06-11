from django import template
from xml.dom import minidom
from urllib import urlopen
from django.views.decorators.cache import cache_page

register = template.Library()


@cache_page(60 * 60)
@register.inclusion_tag("wheather.html", takes_context=False)
def wheather_tallin():
    problem = False
    url = "http://www.ilmateenistus.ee/ilma_andmed/xml/observations.php"
    try:
        dom = minidom.parse(urlopen(url))
        name = dom.getElementsByTagName('name')
        for index, node in enumerate(name):
            if node.firstChild.nodeValue == "Tallinn-Harku":
                airtemperature = dom.getElementsByTagName('airtemperature')
                t = airtemperature[index].firstChild.nodeValue
    except Exception, e:
        problem = True

    return {'t': t, 'problem': problem}
