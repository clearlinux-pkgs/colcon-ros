#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-ros
Version  : 0.3.8
Release  : 14
URL      : https://files.pythonhosted.org/packages/fe/10/976b039be1505ad798f2a2b245c3c66ffbc5f7e49ef57042419313e6d103/colcon-ros-0.3.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/fe/10/976b039be1505ad798f2a2b245c3c66ffbc5f7e49ef57042419313e6d103/colcon-ros-0.3.8.tar.gz
Summary  : Extension for colcon to support ROS packages.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-ros-python = %{version}-%{release}
Requires: colcon-ros-python3 = %{version}-%{release}
Requires: catkin_pkg
Requires: colcon-cmake
Requires: colcon-core
Requires: colcon-pkg-config
Requires: colcon-python-setup-py
Requires: colcon-recursive-crawl
BuildRequires : buildreq-distutils3

%description
colcon-ros
==========
An extension for `colcon-core <https://github.com/colcon/colcon-core>`_ to support `ROS packages <http://www.ros.org>`_.

%package python
Summary: python components for the colcon-ros package.
Group: Default
Requires: colcon-ros-python3 = %{version}-%{release}

%description python
python components for the colcon-ros package.


%package python3
Summary: python3 components for the colcon-ros package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-ros package.


%prep
%setup -q -n colcon-ros-0.3.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551476458
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
