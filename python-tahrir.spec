%global modname tahrir

Name:             python-tahrir
Version:          0.1.8
Release:          1%{?dist}
Summary:          A pyramid app for issuing your own Open Badges

Group:            Development/Languages
License:          AGPLv3+
URL:              http://pypi.python.org/pypi/tahrir
Source0: http://pypi.python.org/packages/source/t/tahrir/%{modname}-%{version}.tar.gz

BuildArch:        noarch


BuildRequires:    python2-devel
BuildRequires:    python-setuptools

Requires: python-pyramid
Requires: python-tahrir-api
Requires: python-sqlalchemy
Requires: python-transaction
Requires: python-pyramid-tm
Requires: python-zope-sqlalchemy
Requires: python-weberror
Requires: python-tw2-sqla
Requires: python-formencode


%description
tahrir
======

tahrir is `Arabic for Liberation
<http://en.wikipedia.org/wiki/Tahrir_Square>`_.

tahrir is also a `Pyramid <http://www.pylonsproject.org/>`_ app for issuing
your own `Open Badges <https://wiki.mozilla.org/Badges>`_.

The name is total overkill.

%prep
%setup -q -n %{modname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc README.rst LICENSE

%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*


%changelog
* Mon Jul 23 2012 rossdylan <rdelinge@redhat.com> 0.1.8-1
- Versioning typo in rpm fixed
- Misc bug fixes 
- Custom 404 page
- oauth authentication, defaults to FAS
* Wed Jun 20 2012 rossdylan <rossdylan@csh.rit.edu> 0.1.6-1
- initial package for Fedora
