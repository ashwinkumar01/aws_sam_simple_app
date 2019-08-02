import json

import pytest

from interview_functions import ackermann, factorial, fib


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{ "test": "body"}',
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "GET",
            "stage": "prod",
        },
        "pathParameters": {"proxy": "/examplepath", "number": "9"},
        "path": "/examplepath",
    }


def test_factorial_function_returns_correct_solution(apigw_event):
    ret = factorial.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 200
    assert data == 362880


def test_factorial_function_raises_400_on_negative_num(apigw_event):
    apigw_event['pathParameters']['number'] = "-1"
    ret = factorial.lambda_handler(apigw_event, "")
    assert ret["statusCode"] == 400


def test_factorial_function_raises_400_for_0(apigw_event):
    apigw_event['pathParameters']['number'] = "0"
    ret = factorial.lambda_handler(apigw_event, "")
    assert ret["statusCode"] == 400


def test_factorial_function_returns_400_on_text(apigw_event):
    apigw_event['pathParameters']['number'] = "test"
    ret = factorial.lambda_handler(apigw_event, "")
    assert ret["statusCode"] == 400
    

def test_fibonacci_function_returns_correct_solution(apigw_event):
    ret = fib.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 200
    assert data == 34


def test_fibonacci_function_raises_400_on_negative_num(apigw_event):
    apigw_event['pathParameters']['number'] = "-1"
    ret = fib.lambda_handler(apigw_event, "")
    assert ret["statusCode"] == 400


def test_fibonacci_function_returns_0_for_0(apigw_event):
    apigw_event['pathParameters']['number'] = "0"
    ret = fib.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 200
    assert data == 0


def test_fibonacci_function_returns_400_on_text(apigw_event):
    apigw_event['pathParameters']['number'] = "test"
    ret = fib.lambda_handler(apigw_event, "")
    assert ret["statusCode"] == 400
    
    
def test_ackermann_function_returns_correct_solution(apigw_event):
    apigw_event['pathParameters']['split_nums'] = "2-2"
    ret = ackermann.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 200
    assert data == 7


def test_ackermann_function_raises_400_on_negative_num(apigw_event):
    apigw_event['pathParameters']['split_nums'] = "2--2"
    ret = ackermann.lambda_handler(apigw_event, "")
    assert ret["statusCode"] == 400


def test_ackermann_function_returns_400_on_text(apigw_event):
    apigw_event['pathParameters']['split_nums'] = "test"
    ret = ackermann.lambda_handler(apigw_event, "")
    assert ret["statusCode"] == 400

