from flask import jsonify
from flask import Flask, request
app = Flask(__name__)
from ingredient import Ingredient
from product import Product

from flask.json import JSONEncoder

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        print (type(obj))
        if isinstance(obj, Product):
            return obj.to_dict()
        return super(MyJSONEncoder, self).default(obj)

app.json_encoder = MyJSONEncoder

@app.route("/search", methods=['GET'])
def search():
    ingredient = request.args.get('ingredient', default = 'organic bananas', type=str)
    app.logger.debug(f'searching for {ingredient}')
    ingredient  = Ingredient.retrieve_by_name(ingredient)
    if ingredient:
        products = Product.search_contains_ingredient(ingredient.id)
        return jsonify({'total': len(products), 'products': products})
    else:
        return jsonify([])


if __name__ == "__main__":
    app.run(host='localhost', port=8080)

