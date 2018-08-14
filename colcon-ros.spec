#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-ros
Version  : 0.3.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/c9/d5/5e79f08b0ddfbd99d9284a01b06ee10e44ac23c02f476e84f72892acf7c1/colcon-ros-0.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/c9/d5/5e79f08b0ddfbd99d9284a01b06ee10e44ac23c02f476e84f72892acf7c1/colcon-ros-0.3.2.tar.gz
Summary  : Extension for colcon to support ROS packages.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-ros-python3
Requires: colcon-ros-python
Requires: catkin_pkg
Requires: colcon-cmake
Requires: colcon-core
Requires: colcon-pkg-config
Requires: colcon-python-setup-py
Requires: colcon-recursive-crawl
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
%setup -q -n colcon-ros-0.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534286731
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
