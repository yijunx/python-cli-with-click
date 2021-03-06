from setuptools import setup

setup(
    name='helloworld',
    version='1.0',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hello=hello:cli
    ''',  
    # here hello=hello:cli -> means hello (the left hand side hello) in the console is mapped to cli function in the hello.py
    # we can use rich to make the output colorful
)