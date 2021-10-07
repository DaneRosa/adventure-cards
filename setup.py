import setuptools
  
with open("README.md", "r") as fh:
    long_description = fh.read()
  
setuptools.setup(
    name="adventure-cards",
    version="0.0.3",
    author="Dane Rosa",
    author_email="dane.c.rosa@gmail.com",
    description="build",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Adventure-Cards",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)