from werkzeug.exceptions import HTTPException
from flask import make_response


class NotFound(HTTPException):
    def __init__(self, status_code, error_message):
        self.response = make_response(error_message, status_code)


class ValidationError(HTTPException):
    def __init__(self, status_code, error_code, error_message):
        message = {"error_code": error_code, "error_message": error_message}
        self.response = make_response(message, status_code)


class InternalServerError(HTTPException):
    def __init__(self, error_code, error_message):
        message = {"error_code": error_code, "error_message": error_message}
        self.response = make_response(message, 500)


class Unauthorized(HTTPException):
    def __init__(self, error_message):
        self.response = make_response(error_message, 401)

class BadRequest(HTTPException):
    def __init__(self, error_message):
        self.response = make_response(error_message, 400)
