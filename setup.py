from setuptools import setup, find_packages

setup(
        name="pieoffice",
        version="0.6",
        license="MIT",
        author="Caio Geraldes",
        author_email="caiogeraldes@protonmail.com",
        packages=find_packages(),
        entry_points={
        'console_scripts': [
           'pieoffice=pieoffice.__main__:main'
            ]
        },
)
