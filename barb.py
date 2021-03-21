from average5e import d, calculageAverage, calculageAverageAdvantage

def getSwordBarb():
  # Changes by level:
  # 01: AC 14, proficiency 2, rage 2
  # 02: reckless
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, Extra Attack
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4, rage 3, brutal1
  # 13: AC 19, proficiency 5, brutal2
  # 16: rage 4
  # 17: AC 20, proficiency 6, brutal3
  # 20: primal rage 24

  b01 = calculageAverage(14, 5, [(1, 8)], 5)
  b02 = calculageAverage(14, 5, [(1, 8)], 5)
  b04 = calculageAverageAdvantage(15, 6, [(1, 8)], 6)
  b05 = 2 * calculageAverageAdvantage(16, 7, [(1, 8)], 6)
  b08 = 2 * calculageAverageAdvantage(17, 8, [(1, 8)], 7)
  b09 = 2 * (calculageAverageAdvantage(18, 9, [(1, 8)], 8) + 0.098 * d(1, 8))
  b13 = 2 * (calculageAverageAdvantage(19, 10, [(1, 8)], 8) + 0.098 * d(2, 8))
  b16 = 2 * (calculageAverageAdvantage(19, 10, [(1, 8)], 9) + 0.098 * d(2, 8))
  b17 = 2 * (calculageAverageAdvantage(20, 11, [(1, 8)], 9) + 0.098 * d(3, 8))
  b20 = 2 * (calculageAverageAdvantage(20, 15, [(1, 8)], 13) + 0.098 * d(3, 8))

  return [b01, b02, b02, b04, b05, b05, b05, b08, b09, b09, b09, b09, b13, b13, b13, b16, b17, b17, b17, b20]

def getGWMBarb():
  # Changes by level:
  # 01: AC 14, proficiency 2, rage 2
  # 02: reckless
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, Extra Attack
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4, rage 3, brutal1
  # 12: ASI
  # 13: AC 19, proficiency 5, brutal2
  # 16: rage 4
  # 17: AC 20, proficiency 6, brutal3
  # 20: primal rage 24

  b01 = calculageAverage(14, 5, [(1, 12)], 5)
  b02 = calculageAverageAdvantage(14, 5, [(1, 12)], 5)
  b04 = calculageAverageAdvantage(15, 6, [(1, 12)], 6)
  b05 = 2 * calculageAverageAdvantage(16, 7, [(1, 12)], 6)
  b08 = 2 * calculageAverageAdvantage(17, 8, [(1, 12)], 7)
  b09 = 2 * (calculageAverageAdvantage(18, 9, [(1, 12)], 8) + 0.098 * d(1, 12))
  b12 = 2 * (calculageAverageAdvantage(18, 4, [(1, 12)], 18) + 0.098 * (d(1, 12) + (calculageAverageAdvantage(18, 4, [(1, 12)], 18) + 0.098 * d(1, 12))))
  b13 = 2 * (calculageAverageAdvantage(19, 5, [(1, 12)], 18) + 0.098 * (d(2, 12) + (calculageAverageAdvantage(19, 5, [(1, 12)], 18) + 0.098 * d(2, 12))))
  b16 = 2 * (calculageAverageAdvantage(19, 5, [(1, 12)], 19) + 0.098 * (d(2, 12) + (calculageAverageAdvantage(19, 5, [(1, 12)], 19) + 0.098 * d(2, 12))))
  b17 = 2 * (calculageAverageAdvantage(20, 6, [(1, 12)], 19) + 0.098 * (d(3, 12) + (calculageAverageAdvantage(20, 6, [(1, 12)], 19) + 0.098 * d(3, 12))))
  b20 = 2 * (calculageAverageAdvantage(20, 10, [(1, 12)], 23) + 0.098 * (d(3, 12) + (calculageAverageAdvantage(20, 10, [(1, 12)], 23) + 0.098 * d(3, 12))))

  return [b01, b02, b02, b04, b05, b05, b05, b08, b09, b09, b09, b12, b13, b13, b13, b16, b17, b17, b17, b20]