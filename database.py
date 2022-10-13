from jsonschema import ValidationError, validate

from error import UnsupportedRequestError

VALIDTION_SCHEMA = {
    "order": {
        "type": "object",
        "properties": {
            "orde_id": {"type": "integer",
                         "minimum": 2},
            "name": {"type": "string",
                     "maxLength": 100},
            "cost": {
                "type": "string",
            }
        },
        "required": ["orde_id", "name", "cost"],
        "additionalProperties": False
    },

}


def validate_request_body(orders, body):
    if not body:
        raise UnsupportedRequestError("Request body cannot be empty")
    valid_schema = VALIDTION_SCHEMA[orders]
    try:
        validate(instance=body, schema=valid_schema)
    except ValidationError as exc:
        raise UnsupportedRequestError(exc.message)