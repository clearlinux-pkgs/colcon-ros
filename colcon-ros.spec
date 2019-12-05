#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-ros
Version  : 0.3.14
Release  : 23
URL      : https://files.pythonhosted.org/packages/e9/17/577c13845ed8612505a925e75a0afcbf3ba67cedeef4dc5f3e3ef5382f78/colcon-ros-0.3.14.tar.gz
Source0  : https://files.pythonhosted.org/packages/e9/17/577c13845ed8612505a925e75a0afcbf3ba67cedeef4dc5f3e3ef5382f78/colcon-ros-0.3.14.tar.gz
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
BuildRequires : colcon-cmake
BuildRequires : colcon-core
BuildRequires : colcon-pkg-config
BuildRequires : colcon-python-setup-py
BuildRequires : colcon-recursive-crawl

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
%setup -q -n colcon-ros-0.3.14
cd %{_builddir}/colcon-ros-0.3.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574693658
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
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
