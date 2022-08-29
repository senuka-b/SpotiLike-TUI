import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

x = setuptools.find_packages()
x.append("spotilike.interface")

setuptools.setup(
    name="SpotiLike",
    version="1.0.0",
    author="Yeti",
    description="Save Spotify songs on-the-go while you're listening, to your Liked Songs library or your favourite playlists with custom hotkeys all through your keyboard!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yetimeh/SpotiLike",
    project_urls={
        "Home Page": "https://github.com/yetimeh/SpotiLike",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=x,
    install_requires=open("./requirements.txt").readlines(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "spotilike = spotilike.main",
        ],
    },
)
