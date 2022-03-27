import unittest

# 리스트를 받았을때, 이 리스트에 fruit이 몇개 들어있는지 세어줘
# (['사과', '딸기', '딸기'], '딸기') -> 2
# (['사과', '딸기', '딸기'], '사과') -> 1
def count_fruit(lst, fruit):
  counter = {}
  for f in lst:
    if f in counter:
      counter[f] += 1
    else:
      counter[f] = 1
  if fruit not in counter:
    return 0
  return counter[fruit]

class TestDouble(unittest.TestCase):
  def test_count_correct(self):    
    self.assertEqual(count_fruit(['사과', '딸기', '딸기'], '사과'), 1)
    self.assertEqual(count_fruit(['사과', '딸기', '딸기'], '딸기'), 2)

  def test_count_empty(self):    
    self.assertEqual(count_fruit([], '사과'), 0)

  def test_count_dne(self):    
    self.assertEqual(count_fruit(['사과'], '바나나'), 0)