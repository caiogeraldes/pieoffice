from setuptools import setup, find_packages

setup(
        name="pieoffice",
        description="A terminal based script converter for ancient (Proto-)Indo-European languages.",
        version="1.0.1",
        license="MIT",
        author="Caio Geraldes",
        author_email="caiogeraldes@protonmail.com",
        packages=find_packages(),
        entry_points={
        'console_scripts': [
           'pieoffice=pieoffice.__main__:main'
            ]
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.6",
)
