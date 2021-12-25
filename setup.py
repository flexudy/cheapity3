from distutils.core import setup
import setuptools

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='cheapity3',
    version='0.0.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
    url='https://flexudy.com',
    license='',
    author='Flexudy Education',
    author_email='support@flexudy.com',
    description='Module generates text like GPT',
    install_requires=REQUIREMENTS
)
