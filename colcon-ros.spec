#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-ros
Version  : 0.2.11
Release  : 2
URL      : https://files.pythonhosted.org/packages/9e/98/2dc17c598b62dc43f31d818bd537b2136c107eb4485c8e6e1e22ab4ccbba/colcon-ros-0.2.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/9e/98/2dc17c598b62dc43f31d818bd537b2136c107eb4485c8e6e1e22ab4ccbba/colcon-ros-0.2.11.tar.gz
Summary  : Extension for colcon to support ROS packages.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-ros-python3
Requires: colcon-ros-python
Requires: catkin_pkg
BuildRequires : buildreq-distutils3

%description
==========

%package python
Summary: python components for the colcon-ros package.
Group: Default
Requires: colcon-ros-python3

%description python
python components for the colcon-ros package.


%package python3
Summary: python3 components for the colcon-ros package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-ros package.


%prep
%setup -q -n colcon-ros-0.2.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532979677
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
