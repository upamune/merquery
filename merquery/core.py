from urllib.parse import urlencode
from enum import Enum

class ItemCondition(Enum):
	ALL = 'condition_all'
	NEW = 'item_condition_id[1]'
	LIKE_NEW = 'item_condition_id[2]'
	GOOD = 'item_condition_id[3]'
	FAIR = 'item_condition_id[4]'
	POOR = 'item_condition_id[5]'
	VERY_POOR = 'item_condition_id[6]'

class ItemStatus(Enum):
	ALL = 'status_all'
	ON_SALE = 'status_on_sale'
	SOLD_OUT = 'status_trading_sold_out'

class ShippingPayer(Enum):
	ALL = 'shipping_payer_all'
	BUYER = 'shipping_payer_id[1]'
	SELLER = 'shipping_payer_id[2]'


class ItemOrder(Enum):
	LOWESET_PRICE = 'price_asc'
	HIGHEST_PRICE = 'price_desc'
	OLDEST = 'created_asc'
	NEWEST = 'created_desc'
	LIKES = 'like_desc'

class Merquery:
	__queries={}

	def __init__(self, host: str='https://www.mercari.com', region: str='jp', search_path: str='search'):
		self.host=host
		self.region=region
		self.search_path=search_path
		return None

	def keyword(self, keyword: str):
		self.__queries['keyword']=keyword
		return self

	def max_price(self, price: int):
		self.__queries['price_max']=price
		return self

	def min_price(self, price: int):
		self.__queries['price_min']=price
		return self

	def status(self, status: ItemStatus):
		if not isinstance(status, ItemStatus):
			raise Exception('status is not member of ItemStatus')
		self.__queries[status.value] = 1
		return self

	def shipping_payer(self, payer: ShippingPayer):
		if not isinstance(payer, ShippingPayer):
			raise Exception('payer is not member of ShippingPayer')
		self.__queries[payer.value] = 1
		return self

	def condition(self, condition: ItemCondition):
		if not isinstance(condition, ItemCondition):
			raise Exception('condition is not member of ItemCondition')
		self.__queries[condition.value] = 1
		return self

	def brand_name(self, name: str):
		self.__queries['brand_name'] = name
		return self

	def order(self, order: ItemOrder):
		if not isinstance(order, ItemOrder):
			raise Exception('order is not member of ItemOrder')
		self.__queries['sort_order'] = order.value
		return self

	def build(self):
		self.__validate_queries()
		queries = self.__get_query_str()
		self.__queries = {}
		base_url=self.__urljoin(self.host, self.region, self.search_path, '?')
		return base_url + queries

	def __validate_queries(self):
		keyword = self.__get_query('keyword')
		if keyword == None or keyword == "":
			raise Exception('keyword is empty')

		max_price = self.__get_query('price_max')
		if max_price:
			if not isinstance(max_price, int):
				raise Exception('max_price is not int')
			if max_price <= 0:
				raise Exception('max_price should be a  positive number')
	
		min_price = self.__get_query('price_min')
		if min_price:
			if not isinstance(min_price, int):
				raise Exception('min_price is not int')
			if min_price <= 0:
				raise Exception('min_price should be a  positive number')

		if max_price and min_price and max_price <= min_price:
			raise Exception('max_price should be greater than min_price')

		brand_name = self.__get_query('brand_name')
		if brand_name and brand_name == '':
			raise Exception('brand_name is empty')

	def __get_query(self, query: str):
		try:
			q = self.__queries[query]
		except KeyError:
			return None
		return q

	def __get_query_str(self):
		return urlencode(self.__queries)

	def __urljoin(self, *args):
		return '/'.join(s.strip('/') for s in args)

