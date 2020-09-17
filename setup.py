from setuptools import setup, find_packages

setup(
        name="pieoffice",
        version="1.0",
        license="MIT",
        author="Caio Geraldes",
        author_email="caiogeraldes@protonmail.com",
        packages=find_packages(),
        entry_points={
        'console_scripts': [
           'pieoffice=pie-office.__main__:main'
            ]
        },
)
