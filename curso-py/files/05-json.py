import json
from pathlib import Path

# To write json file
# products = [
#     {"id": 1, "name": "Skateboard"},
#     {"id": 2, "name": "Bicycle"},
#     {"id": 3, "name": "Surfboard"}
# ]

# data = json.dumps(products)
# Path("files/products.json").write_text(data)

# To read a json file
data = Path("files/products.json").read_text(encoding="utf-8")
products = json.loads(data)
# print(products)

# To modify a json file
products[0]["name"] = "Happy Murphy"
Path("files/products.json").write_text(json.dumps(products))

# JSON = JavaScrip Object Notation
