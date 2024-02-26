%define 	module	fuse
Summary:	Python interface to FUSE (Filesystem in USErspace)
Summary(pl.UTF-8):	Pythonowy interfejs do FUSE (systemu plików w przestrzeni użytkownika)
Name:		python-%{module}
Version:	1.0.7
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/Python
Source0:	https://github.com/libfuse/python-fuse/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	e463d5fb1ff20df2478cba670eaf56da
URL:		https://github.com/libfuse/python-fuse
BuildRequires:	libfuse-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to FUSE (Filesystem in USErspace).

%description -l pl.UTF-8
Pythonowy interfejs do FUSE (Filesystem in USErspace - systemu plików
w przestrzeni użytkownika).

%prep
%setup -q -n python-fuse-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}-%{release}
cp -p example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}-%{release}
%py_postclean

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
%{_examplesdir}/%{name}-%{version}-%{release}
