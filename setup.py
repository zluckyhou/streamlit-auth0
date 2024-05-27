import setuptools

setuptools.setup(
    name="streamlit-auth0-component-custom",
    version="0.1.0",
    author="John",
    author_email="hou0922@gmail.com",
    description="",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
        "python-jose == 3.3.0"
    ],
)
