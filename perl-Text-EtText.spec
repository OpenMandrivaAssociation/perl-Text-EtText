%define module  Text-EtText
%define upstream_version	2.2

Summary:	%{module} module for perl 
Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	12
License:	GPL
Group:		Development/Perl
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Text/Text-EtText-%{upstream_version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.2-9mdv2010.0
+ Revision: 430602
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.2-8mdv2009.0
+ Revision: 241988
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 2.2-6mdv2008.0
+ Revision: 23803
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.2-5mdk
- Fix SPEC according to Perl Policy
	- Source URL
	- URL
- use mkrel

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 2.2-4mdk
- Rebuild

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.2-3mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.2-2mdk
- rebuild for new auto{prov,req}


