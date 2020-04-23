# Enhancements

## Added Makefile

To speed up development, we added a [Makefile](Makefile) that would programatically stop, remove, build, and re-start our container with a single command, `make reload`. We also added a make command to redploy our app to heroku, `make deploy`. This will reduce a lot of overhead on developers throughout the lifetime of the app.

## Added JSON validation to API

To ensure user input data is safe and valid, we added JSON schema validation using this [library](https://pypi.org/project/jsonschema/). This will prevent users from submiting invalid or missing values when adding or changing blockings in the director view. It uses [decorator functions](app/validate.py) on the Flask endpoints which compares incoming JSON in the request to a predefined [schema](app/schema.py).


## Added error handling to API

Minimal error handling was added to the API routes to prevent poor UX in case the app breaks during runtime errors.
