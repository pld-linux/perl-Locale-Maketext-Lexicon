#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	Maketext-Lexicon
Summary:	Locale::Maketext::Lexicon - use other catalog formats in Maketext
Summary(pl.UTF-8):	Locale::Maketext::Lexicon - używanie innych formatów katalogów w Maketext
Name:		perl-Locale-Maketext-Lexicon
Version:	0.62
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	989642c1a83ddc7f1337d77422ee40cf
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
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

%description -l pl.UTF-8
Ten moduł udostępnia moduły do obsługi słowników, pozwalające czytać z
innych formatów plików lokalizacyjnych, takich jak Gettext, Msgcat
itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Change* README SIGNATURE
%{perl_vendorlib}/%{pdir}/Maketext/*.pm
%{perl_vendorlib}/%{pdir}/Maketext/Lexicon
%{perl_vendorlib}/%{pdir}/Maketext/Extract
%{_bindir}/*
%{_mandir}/man?/*
