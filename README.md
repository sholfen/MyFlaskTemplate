# MyFlaskTemplate
 
It' has following folders
1. config
    - This folder has four config files
        - app.config
        - db.config
        - logger.config
        - sql_commands.config
2. controllers
    - put your controller files here
3. data
    - has a SQLite demo db file
4. log
    - default log file folder
5. models
    - put your business logic codes
6. modules
    - you could put shared utilites function here
7. resources
    - put static files, like pictures, css, js files and so on
8. templates

## Hot to Run It

Just execute the run.py, and then open http://localhost:5566. The test account and password are 'admin', '1234'.

## How to Config a Controller

When you add new controller file, for example /controllers/mycontroller.py. Rember to add code in the /controllers/`__init__`.py:
```python
import mycontroller
```

## Put Static Files

In the resources folder, it has three sub folder: css, js, pic. For example, utils.js is in the path /resources/js/utils.js. The url is http://localhost:5566/resources/js/utils.js.

## Setup View Files

Put your view file in the templates folder, for example /templates/home/Index.pyhtml, and add code:
```python
return render_template('./home/Index.pyhtml')
```