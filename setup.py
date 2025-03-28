from setuptools import setup

with open ("README.md" ,"r", encoding="utf-8")as fh:
    long_descriptiion =fh.read()


AUTHOR_NAME ='SHIVANSHU KUMAR'
SRC_REPO='src'

LIST_OF_REQUIREMENT=['streamlit']

setup( 
    name =SRC_REPO,
    VERSION='0.0.1',
    author=AUTHOR_NAME,
    author_email='shivanshu18srivastava@gmail.com',
    description ='A small example package  for movie recomendation ',
    package =[SRC_REPO],
    
)