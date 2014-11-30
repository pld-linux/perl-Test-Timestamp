#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	Test
%define		pnam	Timestamp
%include	/usr/lib/rpm/macros.perl
Summary:	Test::Timestamp Perl module
Summary(cs.UTF-8):	Modul Test::Timestamp pro Perl
Summary(da.UTF-8):	Perlmodul Test::Timestamp
Summary(de.UTF-8):	Test::Timestamp Perl Modul
Summary(es.UTF-8):	Módulo de Perl Test::Timestamp
Summary(fr.UTF-8):	Module Perl Test::Timestamp
Summary(it.UTF-8):	Modulo di Perl Test::Timestamp
Summary(ja.UTF-8):	Test::Timestamp Perl モジュール
Summary(ko.UTF-8):	Test::Timestamp 펄 모줄
Summary(nb.UTF-8):	Perlmodul Test::Timestamp
Summary(pl.UTF-8):	Moduł Perla Test::Timestamp
Summary(pt.UTF-8):	Módulo de Perl Test::Timestamp
Summary(pt_BR.UTF-8):	Módulo Perl Test::Timestamp
Summary(ru.UTF-8):	Модуль для Perl Test::Timestamp
Summary(sv.UTF-8):	Test::Timestamp Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Test::Timestamp
Summary(zh_CN.UTF-8):	Test::Timestamp Perl 模块
Name:		perl-Test-Timestamp
Version:	1.2
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ec7c96f3d6e218de1a58661eef7fde51
URL:		http://search.cpan.org/dist/Test-Timestamp/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With this module you can create one or more timestamp objects which
can be used to record the exact time when a certain point in your code
was executed.

%description -l pl.UTF-8
Używając tego modułu możesz stworzyć jeden lub więcej obiektów ze
znacznikami czasu, które mogą być użyte do zapamiętania dokładnego
czasu wykonania konkretnej części kodu.

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
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
