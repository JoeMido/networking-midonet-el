%global vendor  MidoNet
%global srcname networking-midonet
%global upstream_version 2015.1.1
%global downstream_version 1.0
%global pkgname python-neutron-plugin-midonet
%global docpath doc/build/html

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_version: %global python2_version %(%{__python2} -c "from distutils.sysconfig import get_python_version; print(get_python_version())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%if 0%{?el7}
%define dist .el7
%endif

Name:           %{pkgname}
Version:        %{upstream_version}.%{downstream_version}
Epoch:          1
Release:        2%{?dist}
Provides:       %{pkgname} = %{version}-%{release}
Summary:        %{vendor} OpenStack Neutron driver

Group:          Applications/System
License:        ASL 2.0
URL:            https://github.com/openstack/%{srcname}
Source0:        http://tarballs.openstack.org/%{srcname}/%{srcname}-stable-kilo.tar.gz
Patch0:         0001-port-security.patch
Patch1:         0002-ml2-mech-driver-stub.patch
Patch2:         0003-l3-service.patch
Patch3:         0004-rem-dup-load-client.patch
Patch4:         0005-ml2-mech-type-driver.patch
Patch5:         0006-ml2-filter-mido-net-type.patch
Patch6:         0007-ml2-move-to-util.patch
Patch7:         0008-ext-gw-mode.patch
Patch8:         0009-fix-upd-hm-log.patch

BuildArch:      noarch
BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Requires:       python-neutron = %{upstream_version}
Requires:       python-midonetclient

%description
This package provides %{vendor} networking driver for OpenStack Neutron

%prep
%setup -q -n %{srcname}-%{upstream_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
%{__python2} setup.py build

%install
rm -rf %{buildroot}
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%attr(-, root, root) %doc LICENSE
%attr(-, root, root) %{python2_sitelib}/midonet
%attr(-, root, root) %{python2_sitelib}/*egg-info
%attr(-, root, root) %{_bindir}/midonet-db-manage
