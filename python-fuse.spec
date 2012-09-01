%define 	module	fuse

# lacking a proper versioning scheme, we use the latest changelog entry date
%define		snap	20070119
%define		rel		1

Summary:	Python interface to FUSE (Filesystem in USErspace)
Summary(pl.UTF-8):	Pythonowy interfejs do FUSE (systemu plików w przestrzeni użytkownika)
Name:		python-%{module}
Version:	0.2
Release:	0.1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/f/fuse-python/fuse-python-0.2.tar.gz
# Source0-md5:	68be744e71a42cd8a92905a49f346278
URL:		http://pypi.python.org/pypi/fuse-python/
BuildRequires:	libfuse-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to FUSE (Filesystem in USErspace).

%description -l pl.UTF-8
Pythonowy interfejs do FUSE (Filesystem in USErspace - systemu plików
w przestrzeni użytkownika).

%prep
%setup -q -n fuse-python-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}-%{release}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
install example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}-%{release}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog FAQ README*
%{py_sitedir}/*.py[co]
%{py_sitedir}/fuseparts/*.py[co]
%attr(755,root,root) %{py_sitedir}/fuseparts/*.so
%{py_sitedir}/%{module}_*.egg-info
%{_examplesdir}/%{name}-%{version}-%{release}
