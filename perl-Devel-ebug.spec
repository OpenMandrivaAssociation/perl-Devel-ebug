%define module	Devel-ebug
%define name	perl-%{module}
%define version 0.48
%define rel     1

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Summary:	A simple, extensible Perl debugger 
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl-Proc-Background 
BuildRequires:  perl-String-Koremutake
BuildRequires:  perl-Test-Expect
BuildRequires:  perl-Module-Build
BuildRequires:  perl-Devel-StackTrace
BuildRequires:  perl-YAML
BuildRequires:  perl-Module-Pluggable
BuildRequires:  perl-PadWalker
BuildRequires:  perl(YAML::Syck)
BuildArch:      noarch

%description
A debugger is a computer program that is used to debug other programs. 
Devel::ebug is a simple, extensible Perl debugger with a clean API. Using 
this module, you may easily write a Perl debugger to debug your programs. 

Alternatively, it comes with an interactive debugger, ebug.
%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/Devel
%{_mandir}/*/*
%{_bindir}/*

