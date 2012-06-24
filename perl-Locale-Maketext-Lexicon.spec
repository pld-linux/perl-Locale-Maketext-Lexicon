#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	Maketext-Lexicon
Summary:	Locale::Maketext::Lexicon - use other catalog formats in Maketext
Summary(pl):	Locale::Maketext::Lexicon - u�ywanie innych format�w katalog�w w Maketext
Name:		perl-Locale-Maketext-Lexicon
Version:	0.38
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d21e7bdf3601389bcd8644f30d0623fe
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Ten modu� udost�pnia modu�y do obs�ugi s�ownik�w, pozwalaj�ce czyta� z
innych format�w plik�w lokalizacyjnych, takich jak Gettext, Msgcat
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
