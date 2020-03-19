# Introduction
給定一個點餐句，回傳JSON固定格式的訂單

# Request

```json
{
	"sentence": "我要一杯大杯虎糖醇奶"
}
```


# Response

```json
{
	"data":{
		"total": 1,
		"order": [
			{
				"drink": ["虎糖醇奶茶"],
				"ice": ["去冰", "少冰", "微冰", "正常冰"],
				"sugar": ["正常甜", "少糖", "無糖"],
				"toppings": None,
				"valid": False
			}
		]
	},
	"errorCode": ""
}
```
