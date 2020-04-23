from functools import wraps

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from flask import (
    current_app,
    jsonify,
    request,
)

from schema import schemas


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.json
        except AttributeError as e:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper


def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                validate(request.json, schemas[schema_name])
            except ValidationError as e:
                return jsonify({"error": e.message}), 400
            return f(*args, **kw)
        return wrapper
    return decorator