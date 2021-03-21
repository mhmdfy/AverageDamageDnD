from average5e import plotTo10, plotTo20
from ranger import getSwarmRangerCrossbow, getHorizonRangerStr, getBeastRanger
from rogue import getSwashbucklerTWF, getSwashbucklerRapier
from cleric import getClericGFB, getClericGFBWithLowSpiritWeapon
from barb import getSwordBarb, getGWMBarb
from fighter import getSwordFighter, getCrossbowFighter
from artificer import getArtilleristShooter
from monk import getWayOfHand, getWayOfMercy

plotTo20([\
  (getSwashbucklerTWF(), 'Rogue TWF', 'black'), \
  # (getSwarmRangerCrossbow(), 'Swarmkeeper Crossbow', 'g'), \
  # (getHorizonRangerStr(), 'Horizon GreatWeapon', 'limegreen'), \
  # (getBeastRanger(), 'Beastmaster Longbow', 'darkgreen'), \
  # (getClericGFB(), 'Cleric with GFB', 'b'), \
  # (getSwordBarb(), 'Longsword barbarian', 'orange'), \
  (getSwordFighter(), 'SnB fighter', 'gold'), \
  (getWayOfHand(), 'Flurry of Blows Monk', 'teal'), \
  # (getArtilleristShooter(), 'Artillerist Shooter', 'brown')
  (getCrossbowFighter(), 'Crossbow Fighter', 'brown')
])