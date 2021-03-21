from average5e import d, calculageAverage, calculageAverageAdvantage

def getArtilleristShooter():
  # Changes by level:
  # 01: AC 14, proficiency 2, cantrip scale 1
  # 02: Enhanced Focus +1, Homunculus
  # 03: Eldrich Cannon (2d8), Faerie Fire
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, cantrip scale 2, Arcane Firearm (1d8)
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4, 
  # 10: Enhanced Focus +2
  # 11: cantrip scale 3, Haste
  # 13: AC 19, proficiency 5
  # 15: Double Cannon, Summon Construct
  # 17: AC 20, proficiency 6, cantrip scale 4

  a01 = calculageAverage(14, 5, [(1, 10)], 0)
  a02 = calculageAverage(14, 6, [(1, 10)], 0) + calculageAverage(14, 5, [(1, 4)], 2)
  a03 = calculageAverageAdvantage(14, 6, [(1, 10)], 0) + calculageAverageAdvantage(14, 5, [(2, 8)], 0)
  a04 = calculageAverageAdvantage(15, 7, [(1, 10)], 0) + calculageAverageAdvantage(15, 6, [(2, 8)], 0)
  a05 = calculageAverageAdvantage(16, 8, [(2, 10), (1, 8)], 0) + calculageAverageAdvantage(16, 7, [(2, 8)], 0)
  a08 = calculageAverageAdvantage(17, 9, [(2, 10), (1, 8)], 0) + calculageAverageAdvantage(17, 8, [(2, 8)], 0)
  a09 = calculageAverageAdvantage(18, 10, [(2, 10), (1, 8)], 0) + calculageAverageAdvantage(18, 9, [(2, 8)], 0)
  a10 = calculageAverageAdvantage(18, 11, [(2, 10), (1, 8)], 0) + calculageAverageAdvantage(18, 9, [(2, 8)], 0)
  a11 = 2 * calculageAverage(18, 11, [(3, 10), (1, 8)], 0) + calculageAverage(18, 9, [(2, 8)], 0)
  a13 = 2 * calculageAverage(19, 12, [(3, 10), (1, 8)], 0) + calculageAverage(19, 10, [(2, 8)], 0)
  a15 = calculageAverage(19, 12, [(3, 10), (1, 8)], 0) + 2 * calculageAverage(19, 10, [(2, 8)], 0) + 2 * calculageAverage(19, 10, [(1, 8)], 8)
  a17 = calculageAverage(20, 13, [(4, 10), (1, 8)], 0) + 2 * calculageAverage(20, 11, [(2, 8)], 0) + 2 * calculageAverage(20, 11, [(1, 8)], 8)

  return [a01, a02, a03, a04, a05, a05, a05, a08, a09, a10, a11, a11, a13, a13, a15, a15, a17, a17, a17, a17]