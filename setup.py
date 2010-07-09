import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages

setup(
    name = "django-datagrid",
    version = "0.1.0",
    packages = ['datagrid',
                'datagrid/templatetags',],
    package_data = { 'datagrid': [ 'templates/*.html',
                                     'templates/datagrid/*.html',
                                    ] 
                     },
    zip_safe = False,
    author = "Agiliq Solutions",
    author_email = "hello@agiliq.com",
    description = "A django based datagrid, allowing creating datagrid via a declarative syntax.", 
    url = "http://agiliq.com/",
)
