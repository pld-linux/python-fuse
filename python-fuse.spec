%define 	module	fuse

Summary:	Python interface to FUSE (Filesystem in USErspace)
Name:		python-%{module}
Version:	0.1
Release:	0.1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://richard.jones.name/google-hacks/gmail-filesystem/%{module}-python.tar.gz
# Source0-md5:	932cd7f1997187245206385515865ffd
# Source0-size:	14064
URL:		http://richard.jones.name/google-hacks/gmail-filesystem/gmail-filesystem.html
BuildRequires:	python-devel
BuildRequires:	libfuse-devel
%pyrequires_eq	python-modules
Requires:	libfuse
Requires:	fusermount
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to FUSE (Filesystem in USErspace).

%prep
%setup -q -n %{module}-python

%build
%{py_comp} .
%{py_ocomp} .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{py_sitedir}}
install fuse.py[co] $RPM_BUILD_ROOT%{py_sitescriptdir}
install _fusemodule.so $RPM_BUILD_ROOT%{py_sitedir}/_fusemodule.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*.py[co]
%{py_sitedir}/_fusemodule.so
