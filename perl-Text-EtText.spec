%define module  Text-EtText
%define name	perl-Text-EtText
%define version	2.2
%define release %mkrel 8

Summary:	%{module} module for perl 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
Text::EtText - A perl module to edit html as plain text.

%prep
%setup -q -n Text-EtText-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 
%makeinstall_std

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README doc/* Changes TODO
%{_bindir}/*
%{perl_vendorlib}/Text/*
%_mandir/*/*

