#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	Maketext-Lexicon
Summary:	Locale::Maketext::Lexicon - Use other catalog formats in Maketext
Summary(pl):	Locale::Maketext::Lexicon - u¿ywanie innych formatów katalogów w Maketext
Name:		perl-Locale-Maketext-Lexicon
Version:	0.36
Release:	1
Epoch:		1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	88487388e3e24d5eb88b2ce253dbd0dc
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Locale-Maketext
BuildRequires:	perl-Regexp-Common
BuildRequires:	perl-Test-Simple
# to resolve dependency package name only:
BuildRequires:	perl-Lingua-EN-Sentence
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides lexicon-handling modules to read from other
localization formats, such as Gettext, Msgcat, and so on.

%description -l pl
Ten modu³ udostêpnia modu³y do obs³ugi s³owników, pozwalaj±ce czytaæ z
innych formatów plików lokalizacyjnych, takich jak Gettext, Msgcat
itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Change* README SIGNATURE
%{perl_vendorlib}/%{pdir}/Maketext/*.pm
%{perl_vendorlib}/%{pdir}/Maketext/Lexicon
%{_bindir}/*
%{_mandir}/man?/*
