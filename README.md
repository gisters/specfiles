## rpm-spec

The spec has been tested only on Centos 6 and later.

### How to enable repo

You need to install **epel-release** first.

    yum install epel-release

You have two options to do that:

#### 1. If you're using a version of Linux with dnf:

    dnf copr enable registe/others

You need to have dnf-plugins-core installed.

#### 2. If you have older distribution:

    yum copr enable registe/others

You need to have yum-plugin-copr installed.

#### 3. You can download a repo file on [Fedora Copr](https://copr.fedorainfracloud.org/coprs/registe/others/) and place it to `/etc/yum.repos.d/`.
