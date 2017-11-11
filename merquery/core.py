from urllib.parse import urlencode
from enum import Enum

class ItemStatus(Enum):
	ALL = 'status_all'
	ON_SALE = 'status_on_sale'
	SOLD_OUT = 'status_trading_sold_out'

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
		self.__queries['max_price']=price
		return self

	def min_price(self, price: int):
		self.__queries['min_price']=price
		return self

	def status(self, status: ItemStatus):
		if not isinstance(status, ItemStatus):
			raise Exception('status is not member of ItemStatus')
		self.__queries[status.value] = 1
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

		max_price = self.__get_query('max_price')
		if max_price:
			if not isinstance(max_price, int):
				raise Exception('max_price is not int')
			if max_price <= 0:
				raise Exception('max_price should be a  positive number')
	
		min_price = self.__get_query('min_price')
		if min_price:
			if not isinstance(min_price, int):
				raise Exception('min_price is not int')
			if min_price <= 0:
				raise Exception('min_price should be a  positive number')

		if max_price and min_price and max_price <= min_price:
			raise Exception('max_price should be greater than min_price')
	

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

if __name__ == '__main__':
	mq = Merquery()
	url = mq.max_price(1000).min_price(100).status(ItemStatus.ON_SALE).keyword('秋本帆華').build() 
	print(url)

