from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='1.0',
    description='Data Science Survival Skills Assignment 2',
    author='Muhammad Ghufran Akbar',
    zip_safe=False,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz:math_quiz',
        ],
    },
)