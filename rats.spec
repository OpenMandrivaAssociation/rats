#
# $Id: mondo.spec 1892 2008-03-22 00:57:27Z bruno $
#

Summary:	Rough Auditing Tool for Security
Name:		rats
Version:	2.3
Packager:	Bruno Cornec <bcornec@mandriva.org>
Release:	%mkrel 1
License:	GPL
Group:		Development/C
Url:		https://www.securesoftware.com/
Source:		https://www.fortify.com/downloads2/public/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
BuildRequires:	gcc-c++,libexpat1
Requires:	expat
Patch0:		build.patch

%description
RATS is a tool for scanning C, C++, Perl, PHP, Python 
and Ruby source code and flagging common security related programming
errors such as buffer overflows and TOCTOU (Time Of Check, Time Of
Use) race conditions.  As its name implies, the tool performs only a
rough analysis of source code.  It will not find every error and will
also find things that are not errors.  Manual inspection of your code
is still necessary, but greatly aided with this tool.

%prep
%setup -q
%patch0

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README*

%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

%changelog
