import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      # Expected price calculation
      expected_price = (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2
      self.assertEqual(price, expected_price)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, float(quote['top_bid']['price']))
      self.assertEqual(ask_price, float(quote['top_ask']['price']))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      expected_price = (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2
      self.assertEqual(price, expected_price)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, float(quote['top_bid']['price']))
      self.assertEqual(ask_price, float(quote['top_ask']['price']))


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_bothPricesEqual(self):
        quote = {
            'top_ask': {'price': 100.0, 'size': 50},
            'top_bid': {'price': 100.0, 'size': 50},
            'stock': 'XYZ'
        }
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(price, 100.0)  # Expecting average price to be the same as both bid and ask
        self.assertEqual(stock, 'XYZ')
        self.assertEqual(bid_price, 100.0)
        self.assertEqual(ask_price, 100.0)

    def test_getDataPoint_askPriceLowerThanBid(self):
        quote = {
            'top_ask': {'price': 95.0, 'size': 50},
            'top_bid': {'price': 100.0, 'size': 50},
            'stock': 'ABC'
        }
        stock, bid_price, ask_price, price = getDataPoint(quote)
        expected_price = (100.0 + 95.0) / 2
        self.assertEqual(price, expected_price)  # Average price
        self.assertEqual(stock, 'ABC')
        self.assertEqual(bid_price, 100.0)
        self.assertEqual(ask_price, 95.0)



if __name__ == '__main__':
    unittest.main()
