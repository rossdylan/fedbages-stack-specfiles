%global modname tahrir_api

Name:             python-tahrir-api
Version:          0.1.7
Release:          1%{?dist}
Summary:          An API for interacting with the Tahrir database

Group:            Development/Languages
License:          AGPLv3+
URL:              http://pypi.python.org/pypi/tahrir-api
Source0:          http://pypi.python.org/packages/source/t/tahrir-api/tahrir-api-%{version}.tar.gz

BuildArch:        noarch


BuildRequires:    python2-devel
BuildRequires:    python-setuptools
Requires: python-pygments
Requires: python-sqlalchemy
Requires: python-zope-sqlalchemy
Requires: python-simplejson
Requires: python-paste-deploy

%description
tahrir-api
==========

API for interacting with the Tahrir database Based on the `Tahrir
<https://github.com/ralphbean/tahrir>`_ database model written by `Ralph
Bean <https://github.com/ralphbean>`_. There are two classes that can be
used in this module. The first is TahrirDatabase class located in
tahrir_api.dbapi and the second is the database model located in
tahrir_api.model. The TahrirDatabase class is a high level way to interact
with the database. The model is used for a slightly more low level way of
interacting with the database. It allows for custom interactions with the
database without having to use the TahrirDatabase class.

%prep
%setup -q -n tahrir-api-%{version}

%build
%{__python} setup.py build 

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc README.rst LICENSE

%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*
%{_bindir}/initialize_tahrir_db

%changelog
* Mon Jul 23 2012 rossdylan <rdelinge@redhat.com> 0.1.7-1
- Lots of misc bug fixes
- consolidated the 2 models back into a single version
- expanded the api to include more ways of interacting with the database
- Removed MySQL-python dependancy since tahrir-api is db agnostic

* Wed Jun 13 2012 rossdylan <rdelinge@redhat.com> 0.1.3.1-1
- initial package for Fedora
