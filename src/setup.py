from setuptools import setup, find_packages

setup (
    name        =   "todobackend",
    version     =   "0.1.0",
    description =   "Todobackend Django REST service",
    packages    =   find_packages(),
    include_package_data    =   True,
    scripts                 =   ["manage.py"],
    install_requires        =   ["Django>=2.2.3",
                                 "django-cors-headers>=3.0.2",
                                 "djangorestframework>=3.9.4",
                                 "mysqlclient>=1.4.2.post1",
                                 "pytz>=2019.1",
                                 "sqlparse>=0.3.0",
                                 "uWSGI>=2.0.18"
                                 ],
    extras_require          =   {
                                    "test": [
                                        "colorama>=0.4.1",
                                        "coverage>=4.5.3",
                                        "django-nose>=1.4.6",
                                        "nose>=1.3.7",
                                        "pinocchio>=0.4.2"
                                    ]
                                }
)