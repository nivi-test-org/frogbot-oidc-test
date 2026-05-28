from setuptools import setup, find_packages

setup(
    name='frogbot-oidc-test',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.28.0',
        'flask==2.0.1',
        'Werkzeug==2.0.1',
        'PyYAML==6.0.1',
        'pillow==12.2.0',
    ],
)
