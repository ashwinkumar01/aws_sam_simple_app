def return_payload(status_code: int, message: str):
    """
    Construct return payload with given status code and message and return.
    """
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": message,
    }


def calculate_factorial(num: int, factorial_value: int):
    """
    Return factorial for given number
    calculate_factorial(4) will return 24
     """
    if num <= 1:
        return factorial_value

    return calculate_factorial(num - 1, num * factorial_value)


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc:
        https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    fib_num = event['pathParameters']['number']

    if not fib_num.isdigit() or int(fib_num) < 1:
        return return_payload(400, 'Enter a valid non-negative number')

    num = calculate_factorial(int(fib_num), 1)
    return return_payload(200, str(num))
