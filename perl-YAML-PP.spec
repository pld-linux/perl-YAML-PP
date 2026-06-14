#
# Conditional build:
%bcond_without	tests		# unit tests
#
%define	pdir	YAML
%define	pnam	PP
Summary:	YAML::PP - modular YAML 1.2 processor
Summary(pl.UTF-8):	YAML::PP - modularny procesor YAML-a 1.2
Name:		perl-YAML-PP
Version:	0.40.0
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/YAML/TINITA/%{pdir}-%{pnam}-v%{version}.tar.gz
# Source0-md5:	40f281d64cddce19195e4d2bc8d02521
URL:		https://metacpan.org/dist/YAML-PP
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Encode
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-Module-Load
BuildRequires:	perl-Scalar-List-Utils >= 1.07
BuildRequires:	perl-Test-Simple >= 0.98
BuildRequires:	perl-Test-Warn
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Aliases provided by perl-modules
%define		_noautoreq_perl		Tie::StdArray Tie::StdHash

%description
YAML::PP is a modular YAML processor.

It aims to support YAML 1.2 and YAML 1.1. See <https://yaml.org/>.
Some (rare) syntax elements are not yet supported.

WARNING: Most of the inner API is not stable yet.

%description -l pl.UTF-8
YAML::PP to modularny procesor YAML-a.

Celem jest obsługa standardów YAML 1.2 i YAML 1.1, więcej na
<https://yaml.org/>. Niektóre (rzadkie) elementy składni nie są
jeszcze obsługiwane.

UWAGA: większość wewnętrznego API nie jest jeszcze stabilna.

%prep
%setup -q -n %{pdir}-%{pnam}-v%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md SECURITY.md
%attr(755,root,root) %{_bindir}/yamlpp-events
%attr(755,root,root) %{_bindir}/yamlpp-highlight
%attr(755,root,root) %{_bindir}/yamlpp-load
%attr(755,root,root) %{_bindir}/yamlpp-load-dump
%attr(755,root,root) %{_bindir}/yamlpp-parse-emit
%{perl_vendorlib}/YAML/PP.pm
%dir %{perl_vendorlib}/YAML/PP
%{perl_vendorlib}/YAML/PP/Common.pm
%{perl_vendorlib}/YAML/PP/Constructor.pm
%{perl_vendorlib}/YAML/PP/Dumper.pm
%{perl_vendorlib}/YAML/PP/Emitter.pm
%{perl_vendorlib}/YAML/PP/Exception.pm
%{perl_vendorlib}/YAML/PP/Grammar.pm
%{perl_vendorlib}/YAML/PP/Highlight.pm
%{perl_vendorlib}/YAML/PP/Lexer.pm
%{perl_vendorlib}/YAML/PP/Loader.pm
%{perl_vendorlib}/YAML/PP/Parser.pm
%{perl_vendorlib}/YAML/PP/Perl.pm
%{perl_vendorlib}/YAML/PP/Reader.pm
%{perl_vendorlib}/YAML/PP/Render.pm
%{perl_vendorlib}/YAML/PP/Representer.pm
%{perl_vendorlib}/YAML/PP/Schema.pm
%dir %{perl_vendorlib}/YAML/PP/Schema
%{perl_vendorlib}/YAML/PP/Schema/Binary.pm
%{perl_vendorlib}/YAML/PP/Schema/Catchall.pm
%{perl_vendorlib}/YAML/PP/Schema/Core.pm
%{perl_vendorlib}/YAML/PP/Schema/Failsafe.pm
%{perl_vendorlib}/YAML/PP/Schema/Include.pm
%{perl_vendorlib}/YAML/PP/Schema/JSON.pm
%{perl_vendorlib}/YAML/PP/Schema/Merge.pm
%{perl_vendorlib}/YAML/PP/Schema/Perl.pm
%dir %{perl_vendorlib}/YAML/PP/Schema/Tie
%{perl_vendorlib}/YAML/PP/Schema/Tie/IxHash.pm
%{perl_vendorlib}/YAML/PP/Schema/YAML1_1.pm
%dir %{perl_vendorlib}/YAML/PP/Type
%{perl_vendorlib}/YAML/PP/Type/MergeKey.pm
%{perl_vendorlib}/YAML/PP/Writer.pm
%dir %{perl_vendorlib}/YAML/PP/Writer
%{perl_vendorlib}/YAML/PP/Writer/File.pm
%{_mandir}/man3/YAML::PP.3pm*
%{_mandir}/man3/YAML::PP::Common.3pm*
%{_mandir}/man3/YAML::PP::Constructor.3pm*
%{_mandir}/man3/YAML::PP::Emitter.3pm*
%{_mandir}/man3/YAML::PP::Grammar.3pm*
%{_mandir}/man3/YAML::PP::Highlight.3pm*
%{_mandir}/man3/YAML::PP::Perl.3pm*
%{_mandir}/man3/YAML::PP::Schema.3pm*
%{_mandir}/man3/YAML::PP::Schema::Binary.3pm*
%{_mandir}/man3/YAML::PP::Schema::Catchall.3pm*
%{_mandir}/man3/YAML::PP::Schema::Core.3pm*
%{_mandir}/man3/YAML::PP::Schema::Failsafe.3pm*
%{_mandir}/man3/YAML::PP::Schema::Include.3pm*
%{_mandir}/man3/YAML::PP::Schema::JSON.3pm*
%{_mandir}/man3/YAML::PP::Schema::Merge.3pm*
%{_mandir}/man3/YAML::PP::Schema::Perl.3pm*
%{_mandir}/man3/YAML::PP::Schema::Tie::IxHash.3pm*
%{_mandir}/man3/YAML::PP::Schema::YAML1_1.3pm*
%{_mandir}/man3/YAML::PP::Type::MergeKey.3pm*
%{_mandir}/man3/YAML::PP::Writer.3pm*
%{_mandir}/man3/YAML::PP::Writer::File.3pm*
