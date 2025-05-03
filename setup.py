from setuptools import setup, find_packages

setup(
    name="go-django",
    version="0.0.3",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=3.2",
        "djangorestframework>=3.14"
    ],
    description="A modular Django boilerplate with base services, repositories, decorators, and code scaffolding.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sivakumar, Selva",
    author_email="skr.iitg@gmail.com",
    url="https://github.com/skrindra/go-django",
    license="MIT",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
