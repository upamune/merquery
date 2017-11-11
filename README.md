📦 Merquery: *UNOFFICIAL* Mercari(jp) item search query builder
========================


```python
mq = Merquery()
url = mq.max_price(1000).min_price(100).keyword('秋本帆華').build()
print(url)

# Output: https://www.mercari.com/jp/search/?min_price=100&max_price=1000&keyword=%E7%A7%8B%E6%9C%AC%E5%B8%86%E8%8F%AF
```

## Features

- keyword
- max price
- min price
