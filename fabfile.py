'''
    USAGE: fab deploy
           fab deploy:full if complete deployment
'''

from fabric.api import *
import os
import shutil

# env.shell = "/bin/bash -l -i -c"

env.directory = os.path.dirname(os.path.abspath(__file__))
env.project_name = 'geonode'
env.activate = 'source /home/vagrant/.venvs/geonode/bin/activate'

#server
env.hosts = ['vagrant@192.168.1.29']

def production():
    env.branch = '2.4.x-geonode-1.0.0'
    env.directory = '/home/vagrant/cdfgeonode/'
    env.environment = 'geonode'

#Make production default
production()


def install_requirements():
    with cd(env.directory):
        with prefix(env.activate):
            run("pip install -r requirements.txt")

def update_from_repository():
    with cd(env.directory):
        run('git checkout %s' % env.branch)
        run('git pull')

def update_database():
    with cd(env.directory):
        with prefix(env.activate):
            # before syncdb need fixing uninstalling /installing packages
            run("pip uninstall -y python-slugify")
            run("pip uninstall -y awesome-slugify")
            run("pip install --upgrade awesome-slugify==1.6.2")
            run("python manage.py syncdb")
            run("python manage.py migrate")

def init_local():
    install_requirements()
    #TODO:

def collect_static():
    with cd(env.directory):
        with prefix(env.activate):
            run("python manage.py collectstatic --noinput")

def restart_web():
    run("sudo service apache2 restart")

@task(default=True)
def deploy(mode=None):
    update_from_repository()

    if mode == 'full':
        install_requirements()
        update_database()
    collect_static()
    restart_web()
