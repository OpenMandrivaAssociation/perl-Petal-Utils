%define upstream_name    Petal-Utils
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Useful template modifiers for Petal
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Petal/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Date::Format)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Petal)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Escape)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
The Petal::Utils package contains commonly used the Petal manpage modifiers
(or plugins), and bundles them with an easy-to-use installation interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Petal
