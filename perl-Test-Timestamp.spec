%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Timestamp
Summary:	Test::Timestamp Perl module
Summary(cs):	Modul Test::Timestamp pro Perl
Summary(da):	Perlmodul Test::Timestamp
Summary(de):	Test::Timestamp Perl Modul
Summary(es):	M�dulo de Perl Test::Timestamp
Summary(fr):	Module Perl Test::Timestamp
Summary(it):	Modulo di Perl Test::Timestamp
Summary(ja):	Test::Timestamp Perl �⥸�塼��
Summary(ko):	Test::Timestamp �� ����
Summary(no):	Perlmodul Test::Timestamp
Summary(pl):	Modu� Perla Test::Timestamp
Summary(pt):	M�dulo de Perl Test::Timestamp
Summary(pt_BR):	M�dulo Perl Test::Timestamp
Summary(ru):	������ ��� Perl Test::Timestamp
Summary(sv):	Test::Timestamp Perlmodul
Summary(uk):	������ ��� Perl Test::Timestamp
Summary(zh_CN):	Test::Timestamp Perl ģ��
Name:		perl-%{pdir}-%{pnam}
Version:	1.2
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With this module you can create one or more timestamp objects which
can be used to record the exact time when a certain point in your code
was executed.

%description -l pl
U�ywaj�c tego modu�u mo�esz stworzy� jeden lub wi�cej obiekt�w ze
znacznikami czasu, kt�re mog� by� u�yte do zapami�tania dok�adnego
czasu wykonania konkretnej cz�ci kodu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Test/*.pm
%{_mandir}/man3/*
