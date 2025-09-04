STORE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "petId": {
            "type": "integer"
        },
        "quantity": {
            "type": "integer"
        },
        "status": {
            "type": "string",
            "enum": ["approved", "placed"]
        },
        "complete": {
            "type": "boolean"
        },
        "shipDate": {
            "type": "string",
            "format": "date-time"
        }
    },
    "required": ["id", "petId", "quantity", "status","complete"],
    "additionalProperties": False
}