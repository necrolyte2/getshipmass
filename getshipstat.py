import re
import sys

import requests
from bs4 import BeautifulSoup

URL = 'https://wiki.eveonline.com/en/wiki'
STEELPLATEMASS = 2812500
MWDMASS = 50000000

def fetch_stat(statname, shipname):
    r = requests.get(URL + '/' + shipname)
    soup = BeautifulSoup(r.text)
    paragraphs = soup.find_all('p')
    p = '{0}\s+([\d\s]+)(.*)$'.format(statname)
    for paragraph in paragraphs:
        if statname in paragraph:
            return paragraph

def parse_mass(massstr):
    massstr = massstr.encode('utf-8')
    p = '([\d,]+)'
    mass = re.search(p, massstr).groups()[0].replace(',','')
    return mass

def main():
    ship = sys.argv[1]
    m = fetch_stat('Mass', ship)
    shipmass = int(parse_mass(m))
    print '---' + ship + '---'
    h = fetch_stat('Low Slots', ship)
    lowslots = int(parse_mass(h))
    print '\tShip Mass: {0}'.format(shipmass)
    print '\tLow Slots: {0}'.format(lowslots)

    platemass = STEELPLATEMASS * lowslots
    print '\tPlate Mass: {0}'.format(platemass)
    total = shipmass + platemass + MWDMASS
    print '\tTotal Mass(ship+plate+MWD): {0}'.format(total)
    print '\tMass With Higgs Anchor: {0}'.format(total*2)

if __name__ == '__main__':
    main()
