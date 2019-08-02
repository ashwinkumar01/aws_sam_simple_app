import subprocess

import boto3
import click
import os
import webbrowser

from frontend import create_frontend_html_file


@click.command()
@click.option('--bucket-name',
              default='localhost',
              help='Specify existing S3 bucket to upload to (defaults to localhost)')
def deploy(bucket_name: str):
    if bucket_name == 'localhost':
        localhost_base_url = 'http://localhost:3000'

        with open('index.html', 'w') as html_file:
            html_file.write(create_frontend_html_file(f'{localhost_base_url}/fib/'))

        subprocess.Popen('sam local start-api'.split(), stdout=subprocess.PIPE)
        webbrowser.open(f'file://{os.getcwd()}/index.html', new=2)
        return

    _deploy_to_aws_frankfurt(bucket_name)


def _deploy_to_aws_frankfurt(bucket_name: str):
    package_command = f'sam package --output-template-file packaged.yaml --s3-bucket {bucket_name}'
    deploy_command = 'sam deploy --template-file packaged.yaml \
                     --stack-name ashwin-app \
                     --capabilities CAPABILITY_IAM \
                     --region eu-central-1'

    print('Packaging application...')
    subprocess.Popen(package_command.split(), stdout=subprocess.PIPE).wait()

    print('Deploying application (this could take a few minutes)...')
    subprocess.Popen(deploy_command.split(), stdout=subprocess.PIPE).wait()

    _deploy_frontend_to_s3_bucket(bucket_name)
    url = f'http://{bucket_name}.s3-website.eu-central-1.amazonaws.com/'
    print(f'Deployed application at: {url}')
    webbrowser.open(url, new=2)


def _deploy_frontend_to_s3_bucket(bucket_name: str):
    s3 = boto3.resource('s3')

    with open('index.html', 'w') as html_file:
        fib_url, factorial_url, ackermann_url = get_api_urls()
        html_file.write(create_frontend_html_file(factorial_url))

    website_configuration = {
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'index.html'},
    }

    s3.meta.client.upload_file('index.html', bucket_name, 'index.html', ExtraArgs={'ContentType': 'text/html'})
    boto3.client('s3').put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=website_configuration)


def get_api_urls():
    client = boto3.client('cloudformation')

    for outputkey_dict in client.describe_stacks(StackName='ashwin-app')['Stacks'][0]['Outputs']:
        if outputkey_dict['OutputKey'] == 'FactorialApi':
            return outputkey_dict['OutputValue']


if __name__ == '__main__':
    deploy()
