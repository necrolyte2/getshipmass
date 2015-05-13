# getshipmass

Get ship mass from eve wiki

# Install

```
git clone https://github.com/necrolyte2/getshipmass.git
cd getshipmass
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

# Use

```
$> python getshipstat.py Tempest
---Tempest---
	Ship Mass: 99500000
	Low Slots: 6
	Plate Mass: 16875000
	Total Mass(ship+plate+MWD): 166375000
	Mass With Higgs Anchor: 332750000
```

# Get all BS info

```
$> while read ship; do python getshipstat.py $ship; done < shiplist.lst
---Armageddon---
	Ship Mass: 105200000
	Low Slots: 7
	Plate Mass: 19687500
	Total Mass(ship+plate+MWD): 174887500
	Mass With Higgs Anchor: 349775000
---Apocalypse---
	Ship Mass: 97100000
	Low Slots: 7
	Plate Mass: 19687500
	Total Mass(ship+plate+MWD): 166787500
	Mass With Higgs Anchor: 333575000
---Abaddon---
	Ship Mass: 103200000
	Low Slots: 7
	Plate Mass: 19687500
	Total Mass(ship+plate+MWD): 172887500
	Mass With Higgs Anchor: 345775000
---Scorpion---
	Ship Mass: 103600000
	Low Slots: 5
	Plate Mass: 14062500
	Total Mass(ship+plate+MWD): 167662500
	Mass With Higgs Anchor: 335325000
---Raven---
	Ship Mass: 99300000
	Low Slots: 5
	Plate Mass: 14062500
	Total Mass(ship+plate+MWD): 163362500
	Mass With Higgs Anchor: 326725000
---Rokh---
	Ship Mass: 105300000
	Low Slots: 5
	Plate Mass: 14062500
	Total Mass(ship+plate+MWD): 169362500
	Mass With Higgs Anchor: 338725000
---Dominix---
	Ship Mass: 100250000
	Low Slots: 7
	Plate Mass: 19687500
	Total Mass(ship+plate+MWD): 169937500
	Mass With Higgs Anchor: 339875000
---Megathron---
	Ship Mass: 98400000
	Low Slots: 8
	Plate Mass: 22500000
	Total Mass(ship+plate+MWD): 170900000
	Mass With Higgs Anchor: 341800000
---Hyperion---
	Ship Mass: 100200000
	Low Slots: 7
	Plate Mass: 19687500
	Total Mass(ship+plate+MWD): 169887500
	Mass With Higgs Anchor: 339775000
---Typhoon---
	Ship Mass: 100600000
	Low Slots: 7
	Plate Mass: 19687500
	Total Mass(ship+plate+MWD): 170287500
	Mass With Higgs Anchor: 340575000
---Tempest---
	Ship Mass: 99500000
	Low Slots: 6
	Plate Mass: 16875000
	Total Mass(ship+plate+MWD): 166375000
	Mass With Higgs Anchor: 332750000
---Maelstrom---
	Ship Mass: 103600000
	Low Slots: 5
	Plate Mass: 14062500
	Total Mass(ship+plate+MWD): 167662500
	Mass With Higgs Anchor: 335325000
```
