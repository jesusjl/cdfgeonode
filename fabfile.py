'''
    USAGE: fab deploy
           fab deploy:full if complete deployment
'''

from fabric.api import *
import os
import shutil

env.directory = os.path.dirname(os.path.abspath(__file__))
env.project_name = 'cdfgeonode'

#server
env.hosts = ['vagrant@192.168.1.29']

def production():
    env.branch = 'master'
    env.directory = '/home/vagrant/cdfgeonode/'
    env.environment = 'production'

#Make production default
production()


def install_requirements():
    with cd(env.directory):
        run("workon %s && pip install -r requirements.txt" % (env.project_name))

def update_from_repository():
    with cd(env.directory):
        run('git pull')

def update_database():
    with cd(env.directory):
        run("workon %s && python manage.py syncdb -all" % env.project_name)
        run("workon %s && python manage.py migrate -fake" % env.project_name)

def init_local():
    install_requirements()
    #TODO:

def collect_static():
    with cd(env.directory):
        run("workon %s && python manage.py collectstatic --noinput" % (env.project_name))

def restart_webfaction():
    run("service apache2 restart", with_sudo=True)

@task(default=True)
def deploy(mode=None):
    update_from_repository()
    collect_static()
    if mode == 'full':
        install_requirements()
        update_database()
    restart_webfaction()
