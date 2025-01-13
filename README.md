# python-playwright-boilerplate

## How To

Firstly, we need to create a virtual environment in our project

```
python 3 -m venv venv
```


Then install playwright (of course!!!)

```
pip3 install playwright
```


```
playwright install
```


## Run the damn tests!
```
python3 -m pytest tests
```

## Run with the damn pytest!

We need to install pytest-playwright

```
pip install playwright
```

and then :

```
pytest
```

or 

```
pytest --browser chromium 
```


## Playwright codegen

> We can speed up writing of tests by using codegen

If we want to get locators and any 

```
playwright codegen $BASE_URL

```

We can record any session with the recorder in order to create any given steps or code



## Trace Viewer Debugging

We can upload the trace to:

> https://trace.playwright.dev

OR

just pass the --show-trace command



