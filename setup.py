from setuptools import setup


setup(
    name="GPA calculator",
    version='0.5',
    py_modules=[
        'gpa_calculator'
    ],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gpa_calculator=gpa_calculator:cli
    '''
)