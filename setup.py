from setuptools import setup

REQUIRES = [
    'records',
    'structlog'
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/isolodukhin/db_client.git',
    license='MIT',
    author='ilaso',
    author_email='Ilya',
    install_requirements=REQUIRES,
    description='db_client with logger'
)
