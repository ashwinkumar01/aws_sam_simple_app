# AWS SAM Simple App

This is a simple fullstack application that deploys a Lambda function with the help of AWS Serverless Application Model (SAM)
and a static webpage hosted on S3 that is able to send requests to the Lambda function

```bash
.
├── README.md                   <-- This instructions file
├── requirements.txt            <-- Python requirements file
├── frontend.py                 <-- Python function for creating frontend template
├── manage.py                   <-- Main Driver for this application
├── interview_functions         <-- Source code for lambda functions
│   ├── __init__.py
│   ├── ackermann.py            <-- Lambda function for the Ackermann function
│   ├── factorial.py            <-- Lambda function for the factorial function
│   ├── fib.py                  <-- Lambda function for the fibonacci function
├── template.yaml               <-- SAM Template
└── tests                       <-- Unit tests
    └── unit
        ├── __init__.py
        └── test_handlers.py
```

## Requirements

* [AWS CLI](https://aws.amazon.com/cli/)
* [Python 3.6](https://www.python.org/downloads/)
* [Docker](https://www.docker.com/community-edition)
* [AWS SAM](https://github.com/awslabs/serverless-application-model)
* Requirements listed in requirements.txt (pip install -r requirements.txt)

## Running the application
You can view my own hosted solution here: http://testbucketashwin01.s3-website.eu-central-1.amazonaws.com/

### Running locally
```bash
python manage.py
```
Using SAM, the application is packaged and deployed to localhost:3000.
A html file is constructed and opened in your browser that is able to send requests to the application.


Example endpoints you can try:
* `http://localhost:3000/factorial/4`

### Deploying to S3
#### Prerequisites
* An existing public S3 bucket in eu-central-1
Your bucket policy should look like this (replace bucket name with your own)
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForGetBucketObjects",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::testbucketashwin01/*"
        }
    ]
}
```

#### Deploying the application
* The script takes a parameter for the s3 bucket called `bucket-name` and can be run as shown below:
```bash
python manage.py --bucket-name testbucketashwin01
```

### Tests
Pytest is used to run tests. To run it, navigate to the tests folder and run the following command:
```bash
    export PYTHONPATH='../' && pytest
```


### Cleanup
```bash
aws cloudformation delete-stack --stack-name ashwin-app
```