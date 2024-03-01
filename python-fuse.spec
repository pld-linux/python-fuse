#
# Conditional build:
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module
#
%define 	module	fuse
Summary:	Python interface to FUSE (Filesystem in USErspace)
Summary(pl.UTF-8):	Pythonowy interfejs do FUSE (systemu plików w przestrzeni użytkownika)
Name:		python-%{module}
Version:	1.0.7
Release:	2
License:	LGPL v2.1
Group:		Development/Languages/Python
# TODO: use named tarballs
#Source0:	https://github.com/libfuse/python-fuse/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/libfuse/python-fuse/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	e463d5fb1ff20df2478cba670eaf56da
URL:		https://github.com/libfuse/python-fuse
BuildRequires:	libfuse-devel >= 2.1
BuildRequires:	pkgconfig
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to FUSE (Filesystem in USErspace).

%description -l pl.UTF-8
Pythonowy interfejs do FUSE (Filesystem in USErspace - systemu plików
w przestrzeni użytkownika).

%package -n python3-%{module}
Summary:	Python interface to FUSE (Filesystem in USErspace)
Summary(pl.UTF-8):	Pythonowy interfejs do FUSE (systemu plików w przestrzeni użytkownika)
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
Python interface to FUSE (Filesystem in USErspace).

%description -n python3-%{module} -l pl.UTF-8
Pythonowy interfejs do FUSE (Filesystem in USErspace - systemu plików
w przestrzeni użytkownika).

%prep
%setup -q

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
find $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version} -name '*.py' \
        | xargs sed -i '1s|^#!.*python\b|#!%{__python}|'
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
find $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version} -name '*.py' \
        | xargs sed -i '1s|^#!.*python\b|#!%{__python3}|'
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS FAQ README*
%{py_sitedir}/fuse.py[co]
%dir %{py_sitedir}/fuseparts
%{py_sitedir}/fuseparts/*.py[co]
%attr(755,root,root) %{py_sitedir}/fuseparts/*.so
%{py_sitedir}/fuse_python-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS FAQ README*
%{py3_sitedir}/fuse.py
%{py3_sitedir}/__pycache__/fuse.cpython-*.py[co]
%dir %{py3_sitedir}/fuseparts
%{py3_sitedir}/fuseparts/*.py
%attr(755,root,root) %{py3_sitedir}/fuseparts/*.so
%{py3_sitedir}/fuseparts/__pycache__
%{py3_sitedir}/fuse_python-%{version}-py*.egg-info
%{_examplesdir}/python3-%{module}-%{version}
%endif
