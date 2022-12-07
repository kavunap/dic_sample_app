# from fabric.api import run, local, hosts, cd
# from fabric.contrib import django
# from fabric.api import env

# django.project('dic_sample_app')
# import django
# django.setup()

# from task.models import Task

# def print_instances():
#     for instance in Task.objects.all():
#         print(instance.title)

# @hosts('production-server')
# def print_production_instances():
#     with cd('dic_sample_app'):
#         run('fab print_instances')
# # def deploy():
# #     local('whoami')
# def production():
#     env.hosts=['ec2']
# prod/fabfile.py

# prod/fabfile.py

import os
from fabric.contrib.files import sed
from fabric.api import *
# from fabric.api import *

# initialize the base directory
abs_dir_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))


# declare environment global variables

# root user
# env.user = 'kavunap'

# list of remote IP addresses
env.hosts = ['3.142.255.190']

# password for the remote server
# env.password = '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'

# full name of the user
# env.full_name_user = 'kavuna paul'

# user group
# env.user_group = 'deployers'

# user for the above group
# env.user_name = 'kavunap'
env.forward_agent=True

# ssh key path
env.ssh_keys_dir = os.path.join(abs_dir_path, 'ssh-keys')

# SSH Keys
def start_provision():
    """
    Start server provisioning
    """
    # Create a new directory for a new remote server
    env.ssh_keys_name = os.path.join(
        env.ssh_keys_dir, env.host_string + '_prod_key')
    local('ssh-keygen -t rsa -b 2048 -f {0}'.format(env.ssh_keys_name))
    local('cp {0} {1}/authorized_keys'.format(
        env.ssh_keys_name + '.pub', env.ssh_keys_dir))
    # Prevent root SSHing into the remote server
    sed('/etc/ssh/sshd_config', '^UsePAM yes', 'UsePAM no')
    sed('/etc/ssh/sshd_config', '^PermitRootLogin yes',
        'PermitRootLogin no')
    sed('/etc/ssh/sshd_config', '^#PasswordAuthentication no',
        'PasswordAuthentication no')

    install_ansible_dependencies()
    create_deployer_group()
    create_deployer_user()
    upload_keys()
    set_selinux_permissive()
    run('service sshd reload')
    upgrade_server()

def create_deployer_group():
    """
    Create a user group for all project developers
    """
    run('groupadd {}'.format(env.user_group))
    run('mv /etc/sudoers /etc/sudoers-backup')
    run('(cat /etc/sudoers-backup; echo "%' +
        env.user_group + ' ALL=(ALL) ALL") > /etc/sudoers')
    run('chmod 440 /etc/sudoers')

def create_deployer_user():
    """
    Create a user for the user group
    """
    run('adduser -c "{}" -m -g {} {}'.format(
        env.full_name_user, env.user_group, env.user_name))
    run('passwd {}'.format(env.user_name))
    run('usermod -a -G {} {}'.format(env.user_group, env.user_name))
    run('mkdir /home/{}/.ssh'.format(env.user_name))
    run('chown -R {} /home/{}/.ssh'.format(env.user_name, env.user_name))
    run('chgrp -R {} /home/{}/.ssh'.format(
        env.user_group, env.user_name))

def upload_keys():
    """
    Upload the SSH public/private keys to the remote server via scp
    """
    scp_command = 'scp {} {}/authorized_keys {}@{}:~/.ssh'.format(
        env.ssh_keys_name + '.pub',
        env.ssh_keys_dir,
        env.user_name,
        env.host_string
    )
    local(scp_command)

def clone():
    with cd('~/workspace/dive-into-code/aws-deploy'):
        run('git clone -b master git@github.com:kavunap/dic_sample_app.git')

def pull():
    with cd('~/workspace/dive-into-code/aws-deploy'):
        sudo('git pull origin main')

def prepare_deploy():
    # local("./manage.py test dic_sample_app")
    local("git add -p && git commit -m new")
    local("git push")

def deploy():
    run('git pull origin main')