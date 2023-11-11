from setuptools import setup, find_packages

# setup(name='math_quiz',
#         version='1.0',
#         description='data science survival skills assignment 2',
#       author='Muhammad Ghufran Akbar',
#       packages=['math_quiz'],
#       zip_safe = False)

# setup(name='tests_math_quiz',
#         version='1.0',
#         description='data science survival skills assignment 2 tests',
#       author='Muhammad Ghufran Akbar',
#       packages=['tests_math_quiz'],
#       zip_safe = False)

setup(name='math_quiz',
        version='1.0',
        description='data science survival skills assignment 2',
      author='Muhammad Ghufran Akbar',
      zip_safe = False,
      packages=find_packages(include=['math_quiz','tests_math_quiz','math_quiz.*'])
      )