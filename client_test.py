import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       expected = (quote["top_ask"]["price"] + quote["top_bid"]["price"]) / 2
       self.assertEqual(getDataPoint(quote)[-1], expected)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       expected = (quote["top_ask"]["price"] + quote["top_bid"]["price"]) / 2
       self.assertEqual(getDataPoint(quote)[-1], expected)


  """ ------------ Add more unit tests ------------ """
  
  def test_getRatio_price_b_nonZero(self):
    args = [
       { "price_a": 1, "price_b": 2 },
       { "price_a": 2, "price_b": 3 },
    ]
    """ ------------ Add the assertion below ------------ """
    for arg in args:
       expected = arg["price_a"] / arg["price_b"]
       self.assertEqual(getRatio(arg["price_a"],arg["price_b"]), expected)

  def test_getRatio_price_b_isZero(self):
    args = [
       { "price_a": 1, "price_b": 0 },
       { "price_a": 2, "price_b": 0 },
    ]
    """ ------------ Add the assertion below ------------ """
    for arg in args:
       self.assertIsNone(getRatio(arg["price_a"],arg["price_b"]))


if __name__ == '__main__':
    unittest.main()
