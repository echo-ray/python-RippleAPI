from setuptools import setup, find_packages

setup(
    name='python-RippleAPI',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A python interface to rippled using the JSON-RPC API',
    long_description=open('README.md').read(),
    install_requires=['click'],
    url='https://github.com/patrickshuff/python-RippleAPI',
    author='Patrick Shuff',
    author_email='patrick.shuff@gmail.com'
)
