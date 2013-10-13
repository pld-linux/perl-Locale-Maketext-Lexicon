#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Locale
%define		pnam	Maketext-Lexicon
%include	/usr/lib/rpm/macros.perl
Summary:	Locale::Maketext::Lexicon - use other catalog formats in Maketext
Summary(pl.UTF-8):	Locale::Maketext::Lexicon - używanie innych formatów katalogów w Maketext
Name:		perl-Locale-Maketext-Lexicon
Version:	0.96
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Locale/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7b88febfd5bdbb2ed9e2ea197b7f0148
URL:		http://search.cpan.org/dist/Locale-Maketext-Lexicon/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Locale-Maketext >= 1.17
BuildRequires:	perl-Regexp-Common
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Lingua-EN-Sentence >= 0.25
%endif
Requires:	perl-Locale-Maketext >= 1.17
Suggests:	perl-Lingua-EN-Sentence >= 0.25
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
%doc AUTHORS Changes README
%attr(755,root,root) %{_bindir}/xgettext.pl
%{perl_vendorlib}/Locale/Maketext/Extract.pm
%{perl_vendorlib}/Locale/Maketext/Extract
%{perl_vendorlib}/Locale/Maketext/Lexicon.pm
%{perl_vendorlib}/Locale/Maketext/Lexicon
%{_mandir}/man1/xgettext.pl.1p*
%{_mandir}/man3/Locale::Maketext::Extract*.3pm*
%{_mandir}/man3/Locale::Maketext::Lexicon*.3pm*
