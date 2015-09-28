#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipaddress
Version  : 1.0.14
Release  : 7
URL      : https://pypi.python.org/packages/source/i/ipaddress/ipaddress-1.0.14.tar.gz
Source0  : https://pypi.python.org/packages/source/i/ipaddress/ipaddress-1.0.14.tar.gz
Summary  : IPv4/IPv6 manipulation library
Group    : Development/Tools
License  : Python-2.0
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

%package python
Summary: python components for the ipaddress package.
Group: Default

%description python
python components for the ipaddress package.


%prep
%setup -q -n ipaddress-1.0.14

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 test_ipaddress.py || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
