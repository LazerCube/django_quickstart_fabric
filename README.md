
Django Quickstart - Using fabric, Nginx and Gunicorn
====================================================

A git repository to help you get up and running quickly with a Django 1.9 project and fabric, to automate administration task on a server. This repository can turn a clean install of a Debian-based Linux OS into a working web server  capable of serving a Django 1.9 project with only minimal configuring and pre-setup.

Prerequisites
-------------

-   fabric
-   openssh-server


Using fabric
-------------
```
fab <localhost/remote> <full_install/full_upgrade/full_upgrade>
```

When installing for the first time you must define a django config file to use.
In order to do this put `:"<local/production/staging>"` after the your install command.
For Example: `fab remote full_install:"production"` to use your project with its production settings.

Installing fabric
-----------------

An easy way of installing Fabric on a fresh install is by using the default operating system package manager `aptitude`.

```
sudo aptitude install fabric

# Alternatively, you can also use *pip*:
# pip install fabric
```

Installing/Setup for SSH
------------------------

Fabric allows for excellent integration with SSH that allows for streamlining tasks using simple python scripts. SSH is also a key part of any server configuration.

### Creating new user

By default the fabric file will want sign in as a user called "django", but this could be replace with any username you like as lone as you remember to update the fab file to the same name.

```
sudo adduser django
```

The fabric file will need to be able to run with with administrative privilege in order to install successfully. To allow our new new user to do this we need to add it to the "sudo" group.

```
sudo gpasswd -a django sudo
```

### Installing SSH

```
sudo apt-get update
sudo apt-get install openssh-server
```

###  Adding Public Key Authentication

To generate a new key pair, enter the following command at the terminal of your local machine (ie. your computer)

```
shh-keygen
```

Next copy the Public key on your local machine so we can add it to our server. ssh keys are normally generated to `~/.ssh/id_rsa.pub`. To print your public key in your local machine run.

```
cat ~/.ssh/id_rsa.pub
```

This will print your public SSH key, select and copy it to your clipboard. To enable the user of a SSH key to authenticate, you must add the public key to a special file in your user's home directory.

*On the Server*, enter.

```
su - django
```

Create a new directory called `.ssh` and restrict its permissions.

```
mkdir .ssh
chmod 700 .ssh
```

Now open a file in .ssh called authorized_keys with a text editor. We will use `nano` to edit the file.

```
nano .ssh/authorized_keys
```

Now insert your public key here and exit `nano`. In order to restrict permissions to authorized_keys we run.

```
chmod 600 .ssh/authorized_keys
```

You can now run `exit` to logout of your new user.


Configuring SSH
---------------

Begin by creating a backup of the default config, just in case. Next, open the configuration file with your favorite text editor (for this example we will use nano).

```
cp /etc/ssh/sshd_config /etc/ssh/sshd_config_backup
nano /etc/ssh/sshd_config
```

Then, change default port number. This is a basic step that helps to keep your server as secure as possible.
```
#Before
Port 22

# After
Port 25000
```

Next, we need to disable root login, Modify this line to "no" or "without-password" like this to disable root login.

```
#Before
PermitRootLogin yes

#After
PermitRootLogin without-password
```

We can also disable password authentication and allow only SSH keys, giving your server some extra security. Set the following settings to the following values. If these settings are already in the file, set them to "no" rather than add new lines.

```
ChallengeResponseAuthentication no
PasswordAuthentication no
```

Reload SSH

```
service ssh restart
```

Basic Firewall
--------------

SSH - `sudo ufw allow 25000/tcp`

If you plan on running a conventional HTTP web server, you will need to allow access to port 80.

```
sudo ufw allow 80/tcp
```

If you plan to run a web server with SSL/TLS enabled, you should allow traffic to that port as well.

```
sudo ufw allow 443/tcp
```

Enable the firewall.

```
sudo ufw enable
```
