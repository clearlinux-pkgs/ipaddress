#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipaddress
Version  : 1.0.18
Release  : 25
URL      : http://pypi.debian.net/ipaddress/ipaddress-1.0.18.tar.gz
Source0  : http://pypi.debian.net/ipaddress/ipaddress-1.0.18.tar.gz
Summary  : IPv4/IPv6 manipulation library
Group    : Development/Tools
License  : Python-2.0
Requires: ipaddress-legacypython
Requires: ipaddress-python3
Requires: ipaddress-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
ipaddress
=========
Python 3.3+'s [ipaddress](http://docs.python.org/dev/library/ipaddress) for Python 2.6, 2.7, 3.2.

%package legacypython
Summary: legacypython components for the ipaddress package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the ipaddress package.


%package python
Summary: python components for the ipaddress package.
Group: Default
Requires: ipaddress-legacypython
Requires: ipaddress-python3

%description python
python components for the ipaddress package.


%package python3
Summary: python3 components for the ipaddress package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ipaddress package.


%prep
%setup -q -n ipaddress-1.0.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506875953
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 test_ipaddress.py || :
%install
export SOURCE_DATE_EPOCH=1506875953
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
