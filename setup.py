from setuptools import setup, find_packages

setup(
        name="pie_tk",
        version="1.0",
        license="MIT",
        author="Caio Geraldes",
        author_email="caiogeraldes@protonmail.com",
        packages=find_packages(),
        entry_points={
        'console_scripts': [
           'pie_tk=pie_tk.__main__:main'
            ]
        },
)