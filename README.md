# bananas
Searching the lost banana and maybe get a job at a delicious company

# Why this repo?
I've created this git hub so you can see the evolution of the coding.
I started by the fastest implementation to get a proof of concept, it took me around 5-10 minutes
I continued by estructuring the code in classes and adding some documentation
I added more unti tests
I transformed the main script in a small flask app that can search for products that contain an ingredient ( not just organic bananas )

You can see all those steps in teh commits together with the time it took me to implement it (if that is interesting to you).

# To test it
Install a virtual env
>  virtualenv -p ~/.pyenv/versions/3.6.9/bin/python venv36

source it
> source venv36/bin/activate

install dependencies
> pip install --no-cache-dir --no-deps -r requirements.txt

I like to add --no-cache-dir and --no-deps because I have had bad surprises in the past with new dependencies being pulled and messing everything
then execute the server that will run in http://localhost:8080

> export FLASK_ENV=development
> python tests/test_product.py
> python tests/test_ingredient.py
> python app.py

you can then use curl :
curl --request GET --url 'http://localhost:8080/search?ingredient=Organic%20Banana'

Or go directly to a browser: 'http://localhost:8080/search?ingredient=Organic%20Banana'
