#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tempest-lib
Version  : 1.0.0
Release  : 39
URL      : https://files.pythonhosted.org/packages/27/65/6526be48afed32d6479bf005d9cff82c2fb5071a01e50eff82b1b5ba5565/tempest-lib-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/27/65/6526be48afed32d6479bf005d9cff82c2fb5071a01e50eff82b1b5ba5565/tempest-lib-1.0.0.tar.gz
Summary  : OpenStack Functional Testing Library
Group    : Development/Tools
License  : Apache-2.0
Requires: tempest-lib-bin = %{version}-%{release}
Requires: tempest-lib-license = %{version}-%{release}
Requires: tempest-lib-python = %{version}-%{release}
Requires: tempest-lib-python3 = %{version}-%{release}
Requires: Babel
Requires: fixtures
Requires: httplib2
Requires: iso8601
Requires: jsonschema
Requires: os-testr
Requires: oslo.log
Requires: paramiko
Requires: pbr
Requires: six
BuildRequires : Babel
BuildRequires : buildreq-distutils3
BuildRequires : fixtures
BuildRequires : httplib2
BuildRequires : iso8601
BuildRequires : jsonschema
BuildRequires : os-testr
BuildRequires : oslo.log
BuildRequires : paramiko
BuildRequires : pbr
BuildRequires : six

%description
===========
tempest-lib
===========

OpenStack Functional Testing Library

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/tempest-lib
* Source: http://git.openstack.org/cgit/openstack/tempest-lib
* Bugs: http://bugs.launchpad.net/tempest

tempest-lib is a library of common functionality that was originally in tempest
(or similar in scope to tempest)

**As of the 1.0.0 release tempest-lib as a separate repository and project is
deprecated. The library now exists as part of the tempest project, all future
development will occur there. To use the library for future releases update
your imports from tempest_lib to tempest.lib, and add tempest>=10 to your
project requirements**

Features
--------

Some of the current functionality exposed from the library includes:

* OpenStack python-* client CLI testing framework
* subunit-trace: A output filter for subunit streams. Useful in conjunction
                 with calling a test runner that emits subunit
* A unified REST Client
* Utility functions:
  * skip_because: Skip a test because of a bug
  * find_test_caller: Perform stack introspection to find the test caller.
                      common methods

%package bin
Summary: bin components for the tempest-lib package.
Group: Binaries
Requires: tempest-lib-license = %{version}-%{release}

%description bin
bin components for the tempest-lib package.


%package license
Summary: license components for the tempest-lib package.
Group: Default

%description license
license components for the tempest-lib package.


%package python
Summary: python components for the tempest-lib package.
Group: Default
Requires: tempest-lib-python3 = %{version}-%{release}

%description python
python components for the tempest-lib package.


%package python3
Summary: python3 components for the tempest-lib package.
Group: Default
Requires: python3-core
Provides: pypi(tempest-lib)

%description python3
python3 components for the tempest-lib package.


%prep
%setup -q -n tempest-lib-1.0.0
cd %{_builddir}/tempest-lib-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582913203
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
mkdir -p %{buildroot}/usr/share/package-licenses/tempest-lib
cp %{_builddir}/tempest-lib-1.0.0/LICENSE %{buildroot}/usr/share/package-licenses/tempest-lib/57aed0b0f74e63f6b85cce11bce29ba1710b422b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/check-uuid
/usr/bin/skip-tracker

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tempest-lib/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
