%global modname fedbadges

Name:             python-fedbadges
Version:          0.1.4
Release:          1%{?dist}
Summary:          fedmsg consumer for awarding open badges

Group:            Development/Languages
License:          LPGLv2
URL:              http://pypi.python.org/pypi/fedbadges
Source0:          http://pypi.python.org/packages/source/f/fedbadges/%{modname}-%{version}.tar.gz

BuildArch:        noarch


BuildRequires:    python2-devel
BuildRequires:    python-setuptools
Requires:         python-tahrir-api
Requires:         fedmsg


%description
Fedora Badges

This repo contains the consumer and the command nessicary to hook the
fedora badges stack (Tahrir, Tahrir-API, Tahrir-REST) into fedmsg. Included
is an Example consumer which can be used as a template to create more
complex consumers.

%prep
%setup -q -n %{modname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{__mkdir_p} %{buildroot}%{_sysconfdir}/fedmsg.d/
%{__cp} fedmsg.d/*.py %{buildroot}/%{_sysconfdir}/fedmsg.d/.

%files
%{_bindir}/fedmsg-badges
%{_sysconfdir}/fedmsg.d/badges-global.py
%{_sysconfdir}/fedmsg.d/example-badge.py

%doc README.rst

%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*

%config(noreplace) %{_sysconfdir}/fedmsg.d

%changelog
* Mon Aug 06 2012 rossdylan <rdelinge@redhat.com> 0.1.4-1
- Multiple small bugfixes, and it now installs the example config files
* Thu Aug 02 2012 rossdylan <rdelinge@redhat.com> 0.1.1-1
- initial package for Fedora
