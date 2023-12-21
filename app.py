from flask import Flask,request

app = Flask(__name__)

shops = [

{
	"Name": "Laxmi Grocery Store",
	"Pincode": 143001,
	"isActive": True	
},
{
	"Name": "Shammi Garment Store",
	"Pincode": 143001,
	"isActive": True	
}
]

@app.route("/shops")
def get_shops():
	return shops 

@app.route("/shops", methods = ['POST'])
def create_shop():
	shop = request.json
	shops.append(shop)
	return shop, 201


# <shop_name> is the path paremeters
@app.route("/shops/<shop_name>/product",methods=['POST'])
def create_product(shop_name):
	product = request.json
	print(shop_name)
	for shop in shops:
		if shop.get("Name").strip().lower() == shop_name.strip().lower():
			if shop.get('product'):
				shop['product'].append(product)
			else:
				shop['product'] = [product]
			return product

	return {"message":"Shop Not Found"}, 404


@app.route("/shops/<shop_name>")
def get_shop_by_name(shop_name):
	for shop in shops:
		if shop.get("Name").strip().lower() == shop_name.strip().lower():
			return shop, 200

	return {"message":"No Shop Found with the Name"}, 404 





app.run()