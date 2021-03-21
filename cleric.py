from average5e import calculageAverage

def getClericGFB():
  # extra ASI at 12, 16
  # extra 1d8 a turn at level 8, 2d8 at level 14
  c01 = calculageAverage(14, 5, [(2, 6)], 4)
  c03 = calculageAverage(14, 5, [(2, 6)], 4)
  c04 = calculageAverage(15, 6, [(2, 6)], 5)
  c05 = calculageAverage(16, 7, [(2, 6), (2, 8)], 5)
  c07 = calculageAverage(16, 7, [(2, 6), (2, 8)], 5)
  c08 = calculageAverage(17, 8, [(2, 6), (3, 8)], 6)
  c09 = calculageAverage(18, 9, [(2, 6), (3, 8)], 6)
  c11 = calculageAverage(18, 9, [(2, 6), (5, 8)], 6)
  c12 = calculageAverage(18, 9, [(2, 6), (5, 8)], 6)
  c13 = calculageAverage(19, 10, [(2, 6), (5, 8)], 6)
  c14 = calculageAverage(19, 10, [(2, 6), (6, 8)], 6)
  c15 = calculageAverage(19, 10, [(2, 6), (6, 8)], 6)
  c16 = calculageAverage(19, 10, [(2, 6), (6, 8)], 6)
  c17 = calculageAverage(20, 11, [(2, 6), (8, 8)], 6)

  return [c01, c01, c03, c04, c05, c05, c07, c08, c09, c09, c11, c12, c13, c14, c15, c16, c17, c17, c17, c17]

def getClericGFBWithSpiritWeapon():
  # extra bonus (spirit weapon) at 3, 7, 11, 15
  # extra ASI at 12, 16
  # extra 1d8 a turn at level 8, 2d8 at level 14
  c01 = calculageAverage(14, 5, [(2, 6)], 4)
  c03 = calculageAverage(14, 5, [(2, 6)], 4) + calculageAverage(14, 5, [(1, 8)], 3)
  c04 = calculageAverage(15, 6, [(2, 6)], 5) + calculageAverage(15, 5, [(1, 8)], 3)
  c05 = calculageAverage(16, 7, [(2, 6), (2, 8)], 5) + calculageAverage(16, 6, [(1, 8)], 3)
  c07 = calculageAverage(16, 7, [(2, 6), (2, 8)], 5) + calculageAverage(16, 6, [(2, 8)], 3)
  c08 = calculageAverage(17, 8, [(2, 6), (3, 8)], 6) + calculageAverage(17, 6, [(2, 8)], 3)
  c09 = calculageAverage(18, 9, [(2, 6), (3, 8)], 6) + calculageAverage(18, 7, [(2, 8)], 3)
  c11 = calculageAverage(18, 9, [(2, 6), (5, 8)], 6) + calculageAverage(18, 7, [(3, 8)], 3)
  c12 = calculageAverage(18, 9, [(2, 6), (5, 8)], 6) + calculageAverage(18, 8, [(3, 8)], 4)
  c13 = calculageAverage(19, 10, [(2, 6), (5, 8)], 6) + calculageAverage(19, 9, [(3, 8)], 4)
  c14 = calculageAverage(19, 10, [(2, 6), (6, 8)], 6) + calculageAverage(19, 9, [(3, 8)], 4)
  c15 = calculageAverage(19, 10, [(2, 6), (6, 8)], 6) + calculageAverage(19, 9, [(4, 8)], 4)
  c16 = calculageAverage(19, 10, [(2, 6), (6, 8)], 6) + calculageAverage(19, 10, [(4, 8)], 5)
  c17 = calculageAverage(20, 11, [(2, 6), (8, 8)], 6) + calculageAverage(20, 11, [(4, 8)], 5)

  return [c01, c01, c03, c04, c05, c05, c07, c08, c09, c09, c11, c12, c13, c14, c15, c16, c17, c17, c17, c17]

def getClericGFBWithLowSpiritWeapon():
  # extra bonus (spirit weapon) at 5, 9, 13, 17
  # extra ASI at 12, 16
  # extra 1d8 a turn at level 8, 2d8 at level 14
  c01 = calculageAverage(14, 5, [(2, 6)], 4)
  c03 = calculageAverage(14, 5, [(2, 6)], 4)
  c04 = calculageAverage(15, 6, [(2, 6)], 5)
  c05 = calculageAverage(16, 7, [(2, 6), (2, 8)], 5) + calculageAverage(16, 6, [(1, 8)], 3)
  c07 = calculageAverage(16, 7, [(2, 6), (2, 8)], 5) + calculageAverage(16, 6, [(1, 8)], 3)
  c08 = calculageAverage(17, 8, [(2, 6), (3, 8)], 6) + calculageAverage(17, 6, [(1, 8)], 3)
  c09 = calculageAverage(18, 9, [(2, 6), (3, 8)], 6) + calculageAverage(18, 7, [(2, 8)], 3)
  c11 = calculageAverage(18, 9, [(2, 6), (5, 8)], 6) + calculageAverage(18, 7, [(2, 8)], 3)
  c12 = calculageAverage(18, 9, [(2, 6), (5, 8)], 6) + calculageAverage(18, 8, [(2, 8)], 4)
  c13 = calculageAverage(19, 10, [(2, 6), (5, 8)], 6) + calculageAverage(19, 9, [(3, 8)], 4)
  c14 = calculageAverage(19, 10, [(2, 6), (6, 8)], 6) + calculageAverage(19, 9, [(3, 8)], 4)
  c15 = calculageAverage(19, 10, [(2, 6), (6, 8)], 6) + calculageAverage(19, 9, [(3, 8)], 4)
  c16 = calculageAverage(19, 10, [(2, 6), (6, 8)], 6) + calculageAverage(19, 10, [(3, 8)], 5)
  c17 = calculageAverage(20, 11, [(2, 6), (8, 8)], 6) + calculageAverage(20, 11, [(4, 8)], 5)

  return [c01, c01, c03, c04, c05, c05, c07, c08, c09, c09, c11, c12, c13, c14, c15, c16, c17, c17, c17, c17]