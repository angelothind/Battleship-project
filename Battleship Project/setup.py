import setuptools

with open("README.md","r") as fh:
    long_des = fh.read()

setuptools.setup(
    name = "battleship_pkg_at970",
    version = "0.0.1",
    author = "Angelo Singh Thind",
    author_email= "at970@exeter.ac.uk",
    description= "A python implementation of battleship board game",
    long_description= long_des,
    long_description_content_type = "text/markdown"
)