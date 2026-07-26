%define upstream_name    Petal-Utils
Name:		perl-%{upstream_name}
Version:	0.06
Release:	6

Summary:	Useful template modifiers for Petal
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Petal-Utils
Source0:	https://cpan.metacpan.org/authors/id/W/WM/WMCKEE/Petal-Utils-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Date::Format)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Petal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI::Escape)

BuildArch:	noarch

%description
The Petal::Utils package contains commonly used the Petal manpage modifiers
(or plugins), and bundles them with an easy-to-use installation interface.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Petal


%changelog
* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 505297
- rebuild using %0.06 Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.06-3mdv2010.0
+ Revision: 430526
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.06-2mdv2009.0
+ Revision: 268713
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.0
+ Revision: 213779
- import perl-Petal-Utils


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.0
- first mdv release  
