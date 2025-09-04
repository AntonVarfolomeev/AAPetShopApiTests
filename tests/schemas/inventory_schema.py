INVENTORY_SCHEMA = {
    "type": "object",
    "properties": {
        "approved": {
            "type": "integer"
        },
        "delivered": {
            "type": "integer"
        }
    },
    "required": ["approved", "delivered"],
    "additionalProperties": False
}