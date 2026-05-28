from setuptools import setup, find_packages

setup(
    name='frogbot-oidc-test',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.33.0',
        'flask==2.0.1',
        'Werkzeug==2.0.1',
        'PyYAML==6.0.1',
        'Pillow==10.3.0',
    ],
)
