📦 Merquery: *UNOFFICIAL* Mercari(jp) item search query builder
===============================================================


.. image:: https://badge.fury.io/py/merquery.svg
    :target: https://badge.fury.io/py/merquery

Install
-------

.. code-block:: bash

    $ pip install merquery


Usage
-----

.. code-block:: python

    import merquery as mq
    
    q = mq.Merquery()
    url = q.max_price(1000) \
    	    .min_price(100) \
	    .root_category(mq.RootCategory.VINTAGE_AND_COLLECTBLES) \
	    .status(mq.ItemStatus.ON_SALE) \
	    .shipping_payer(mq.ShippingPayer.SELLER) \
	    .condition(mq.ItemCondition.NEW) \
	    .order(mq.ItemOrder.LIKES) \
	    .page(2) \
	    .keyword('秋本帆華') \
	    .build()
    print(url)

    # Output: https://www.mercari.com/jp/search/?item_condition_id%5B1%5D=1&status_on_sale=1&shipping_payer_id%5B2%5D=1&page=2&keyword=%E7%A7%8B%E6%9C%AC%E5%B8%86%E8%8F%AF&sort_order=like_desc&max_price=1000&min_price=100


Supported queries
-----------------

-  keyword
-  max price
-  min price
-  item status
-  shipping payer
-  item condition
-  brand name
-  sort order
-  root category
-  page

Unsupported queries
-------------------

-  size
-  child category
-  grand child category
