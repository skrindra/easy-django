from setuptools import setup, find_packages

setup(
    name="django-boilerplate",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=3.2",
        "djangorestframework>=3.14"
    ],
    description="Reusable Django boilerplate with modular structure and app generator command",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sivakumar, Selva",
    author_email="techsiva33@gmail.com",
    url="https://github.com/skrindra/django-boilerplate",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
