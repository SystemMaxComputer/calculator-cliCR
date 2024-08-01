from setuptools import setup

setup(
    name="cli-calculator",
    version="0.1",
    packages=['calculator', 'tests'],
    install_requires=[
        'click'
    ],
    entry_point='''
    [console_scripts]
    calc= calculator.cli:calc
    '''
)
