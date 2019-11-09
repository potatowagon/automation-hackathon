try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="auto-hackathon",
    version="0.0.1", #to-edit
    packages=["tests"],
    description="applitools automation hackathon",
    long_description="",
    long_description_content_type="text/markdown",
    author="Sherry aka potatowagon",
    author_email="e0007652@u.nus.edu",
    url="https://github.com/potatowagon/automation-hackathon.git",
    keywords=["automation", "hackathon"],
    install_requires=["selenium", "eyes-selenium", "pytest"],
    extras_require={
        "dev": [
            "codecov>=2.0.15",
            "colorama>=0.3.4",
            "tox>=3.9.0",
            "tox-travis>=0.12",
            "pytest-cov>=2.7.1",
        ]
    },
    python_requires=">=3.7",
)