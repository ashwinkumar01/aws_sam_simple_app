import json


def return_payload(status_code: int, message: str):
    """
    Construct return payload with given status code and message and return.
    """
    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": message,
        }),
    }
