Usage
=====

Server
------

- Create user for the deployment i.e. `deployer`

.. code-block:: bash

    adduser deployer

- Add user to the sudoers group:

.. code-block:: bash

    adduser deployer sudo

- Copy your SSH public key to the user's home directory

.. code-block:: bash

    ssh-copy-id deployer@123.456.789

Local
-----

- Install ansible:

.. code-block:: bash

    http://docs.ansible.com/ansible/intro_installation.html

- Specify servers in hosts file:

.. code-block:: bash

    sib-server ansible_ssh_host=123.456.789

    [sib_servers]
    sib-server

- Create variables file in **group_vars** directory. File name should be the same as servers group name.
  For example, for servers group `[sib_servers]` I will create variables file `group_vars/sib_servers`.

  Example of the variables file:

.. code-block:: bash

    db_host: localhost
    db_name: sib
    db_password: sib_password
    db_username: sib_user

    git_repo_url: https://github.com/StoreInBox/sib-main.git
    git_branch: master

    # pip install -r requirements/dev.txt = 1, python setup.py install = 2
    install_type: 2

    project_name: sib-main

    server_name: 123.456.789

- Create a folder with `project_name` in files directory and put settings.py file in it.
  Note that you can use variables from `group_vars/sib_servers` file. For example, for `project_name: sib-main`
  I will create `files/sib-main/settings.py` file.
  Example of valid settings.py file:

.. code-block:: python

    from .base import *

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'x*m*9+#t04u3*80t@phqqh)&q9=do)ot1fjz^s#h5r5wweag8b'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    INTERNAL_IPS = ['http://127.0.0.1:80']

    TEMPLATE_DEBUG = DEBUG

    LANGUAGE_CODE = 'en'

    ALLOWED_HOSTS = []

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '{{ db_name }}',               # Or path to database file if using sqlite3.
            'USER': '{{ db_username }}',           # Not used with sqlite3.
            'PASSWORD': '{{ db_password }}',       # Not used with sqlite3.
            'HOST': '{{ db_host }}',               # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',               # Set to empty string for default. Not used with sqlite3.
        }
    }


- Go to the `django_server.yml` playbook:
    - Check that all files and directory paths are specified correctly.
    - Check that `hosts` is correct and exists in **hosts** file.
    - Run playbook with following command:

    .. code-block:: bash

        ansible-playbook -i hosts django_server.yml --ask-sudo-pass

- You can update your project after running playbook with following command:

.. code-block:: bash

  update-<project_name>-project i.e. update-sib-main-project

