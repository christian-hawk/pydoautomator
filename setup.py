import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydoautomator",
    version="0.3.1",
    author="Christian Eland",
    author_email="eland.christian@gmail.com",
    description="The Digital Ocean automations lib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/christian-hawk/pydoautomator/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pydantic>=1.6.1",
        "requests>=2.24.0"
    ]
)
