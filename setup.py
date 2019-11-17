import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ev3-python",
    version="0.0.1",
    author="Vladislav Bolkunov",
    author_email="vladbolkunovv@gmail.com",
    description="Simple library to control 'Lego™ EV3' controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vladdoth/pyEV3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    install_requres=[
        'pyserial'
    ]
)
