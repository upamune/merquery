📦 Merquery: *UNOFFICIAL* Mercari(jp) item search query builder
========================

```python
mq = Merquery()
url = mq.max_price(1000).min_price(100).status(ItemStatus.ON_SALE).shipping_payer(ShippingPayer.SELLER).condition(ItemCondition.NEW).keyword('秋本帆> 華').build()
print(url)

# Output: https://www.mercari.com/jp/search/?min_price=100&max_price=1000&item_condition_id%5B1%5D=1&shipping_payer_id%5B2%5D=1&keyword=%E7%A7%8B%E6%9C%AC%E5%B8%86%E8%8F%AF&status_on_sale=1
```

## Supported queries

- keyword
- max price
- min price
- item status
- shipping payer
- item condition
- brand name

## Unsupported queries

- size
- category
- sub category

