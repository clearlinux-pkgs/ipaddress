#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipaddress
Version  : 1.0.22
Release  : 51
URL      : http://pypi.debian.net/ipaddress/ipaddress-1.0.22.tar.gz
Source0  : http://pypi.debian.net/ipaddress/ipaddress-1.0.22.tar.gz
Summary  : IPv4/IPv6 manipulation library
Group    : Development/Tools
License  : Python-2.0
Requires: ipaddress-license = %{version}-%{release}
Requires: ipaddress-python = %{version}-%{release}
Requires: ipaddress-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
ipaddress
=========
Python 3.3+'s [ipaddress](http://docs.python.org/dev/library/ipaddress) for Python 2.6, 2.7, 3.2.

%package license
Summary: license components for the ipaddress package.
Group: Default

%description license
license components for the ipaddress package.


%package python
Summary: python components for the ipaddress package.
Group: Default
Requires: ipaddress-python3 = %{version}-%{release}

%description python
python components for the ipaddress package.


%package python3
Summary: python3 components for the ipaddress package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ipaddress package.


%prep
%setup -q -n ipaddress-1.0.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554321130
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 test_ipaddress.py || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipaddress
cp LICENSE %{buildroot}/usr/share/package-licenses/ipaddress/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipaddress/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
