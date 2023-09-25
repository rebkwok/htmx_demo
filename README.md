# The simplest htmx demo

A tiny flask app to demo a very simple htmx call.

`app.py` contains the app and routes - there is just one main view (`home`), which 
renders a page with a (random) coloured dot and a button. Clicking the button submits an
http get request to /partials/change-colour and replaces the dot with another
random colour.


## To run

1. Clone this repo

```
git clone git@github.com:rebkwok/htmx_demo.git
```

2. Install requirements
```
cd htmx_demo
pip install -r requirement.txt
```

3. Run
```
flask run --debug
```
