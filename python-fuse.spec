%define 	module	fuse

# lacking a proper versioning scheme, we use the latest changelog entry date
%define		_snap	20070119

Summary:	Python interface to FUSE (Filesystem in USErspace)
Summary(pl.UTF-8):	Pythonowy interfejs do FUSE (systemu plików w przestrzeni użytkownika)
Name:		python-%{module}
Version:	0.1
Release:	0.%{_snap}.1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://richard.jones.name/google-hacks/gmail-filesystem/%{module}-python.tar.gz
# Source0-md5:	7d2d48b10d7e3ec3b1d04b3efbd6c955
URL:		http://richard.jones.name/google-hacks/gmail-filesystem/gmail-filesystem.html
BuildRequires:	python-devel
BuildRequires:	libfuse-devel
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to FUSE (Filesystem in USErspace).

%description -l pl.UTF-8
Pythonowy interfejs do FUSE (Filesystem in USErspace - systemu plików
w przestrzeni użytkownika).

%prep
%setup -q -n %{module}-python

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
install xmp.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}-%{release}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
%{_examplesdir}/%{name}-%{version}-%{release}
