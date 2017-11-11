📦 Merquery: *UNOFFICIAL* Mercari(jp) item search query builder
========================

```python
mq = Merquery()
url = mq.max_price(1000).min_price(100).status(ItemStatus.ON_SALE).shipping_payer(ShippingPayer.SELLER).condition(ItemCondition.NEW).order(ItemOrder.LIKES).keyword('秋本帆華').build()
print(url)

# Output: https://www.mercari.com/jp/search/?item_condition_id%5B1%5D=1&status_on_sale=1&shipping_payer_id%5B2%5D=1&keyword=%E7%A7%8B%E6%9C%AC%E5%B8%86%E8%8F%AF&sort_order=like_desc&max_price=1000&min_price=100
```

## Supported queries

- keyword
- max price
- min price
- item status
- shipping payer
- item condition
- brand name
- sort order

## Unsupported queries

- size
- category
- sub category

