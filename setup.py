import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mxloadersuite",
    version="0.0.1",
    author="Lee Cotton",
    author_email="lee.cotton@uk.ibm.com",
    description="MXLoader Suite Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lee-cotton/mxloadersuite",
    packages=['mxls'],
        install_required=[
            'requests',
            'openpyxl'
        ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
