# config valid for current version and patch releases of Capistrano
# lock "~> 3.17.1"

# set :application, "my_app_name"
# set :repo_url, "git@example.com:me/my_repo.git"

# Default branch is :master
# ask :branch, `git rev-parse --abbrev-ref HEAD`.chomp

# Default deploy_to directory is /var/www/my_app_name
# set :deploy_to, "/var/www/my_app_name"

# Default value for :format is :airbrussh.
# set :format, :airbrussh

# You can configure the Airbrussh format using :format_options.
# These are the defaults.
# set :format_options, command_output: true, log_file: "log/capistrano.log", color: :auto, truncate: :auto

# Default value for :pty is false
# set :pty, true

# Default value for :linked_files is []
# append :linked_files, "config/database.yml", 'config/master.key'

# Default value for linked_dirs is []
# append :linked_dirs, "log", "tmp/pids", "tmp/cache", "tmp/sockets", "tmp/webpacker", "public/system", "vendor", "storage"

# Default value for default_env is {}
# set :default_env, { path: "/opt/ruby/bin:$PATH" }

# Default value for local_user is ENV['USER']
# set :local_user, -> { `git config user.name`.chomp }

# Default value for keep_releases is 5
# set :keep_releases, 5

# Uncomment the following to require manually verifying the host key before first deploy.
# set :ssh_options, verify_host_key: :secure


set :application, 'DIC_Sample'
# set :scm, :git
set :repo_url, 'https://github.com/kavunap/dic_sample_app.git'
# set :django_settings_dir, 'dic_sample_app/settings'
# set :pip_requirements, 'requirements.txt'
# set :keep_releases, 5
# set :nginx, true
# set :deploy_to, '/www/app_name.com'
# set :wsgi_file, 'dic_sample_app.wsgi'
# set :npm_tasks, {:grunt => 'do_something', :gulp => 'something_else'}
# set :stage, :production
# set :django_settings, 'production'
# role :web, "ec2-user@3.137.134.143"
set :bundle_without, %w{test}.join(':')