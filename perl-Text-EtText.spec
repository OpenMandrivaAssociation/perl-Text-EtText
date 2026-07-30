%define module  Text-EtText
%define upstream_version	2.2

Summary:	%{module} module for perl 
Name:		perl-%{module}
Version:	%{upstream_version}
Release:	1
License:	GPL
Group:		Development/Perl
Source0:	https://cpan.metacpan.org/authors/id/J/JM/JMASON/Text-EtText-2.2.tar.gz
Url:		https://metacpan.org/dist/Text-EtText
BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Text::EtText - A perl module to edit html as plain text.

%prep
%setup -q -n Text-EtText-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%install
%makeinstall_std

%files
%doc README doc/* Changes TODO
%{_bindir}/*
%{perl_vendorlib}/Text/*
%_mandir/*/*



