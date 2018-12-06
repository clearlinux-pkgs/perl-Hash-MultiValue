#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Hash-MultiValue
Version  : 0.16
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/Hash-MultiValue-0.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/Hash-MultiValue-0.16.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhash-multivalue-perl/libhash-multivalue-perl_0.16-1.debian.tar.xz
Summary  : 'Store multiple values per key'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Hash-MultiValue-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Hash::MultiValue - Store multiple values per key
SYNOPSIS
use Hash::MultiValue;

%package dev
Summary: dev components for the perl-Hash-MultiValue package.
Group: Development
Provides: perl-Hash-MultiValue-devel = %{version}-%{release}

%description dev
dev components for the perl-Hash-MultiValue package.


%package license
Summary: license components for the perl-Hash-MultiValue package.
Group: Default

%description license
license components for the perl-Hash-MultiValue package.


%prep
%setup -q -n Hash-MultiValue-0.16
cd ..
%setup -q -T -D -n Hash-MultiValue-0.16 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Hash-MultiValue-0.16/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Hash-MultiValue
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Hash-MultiValue/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Hash/MultiValue.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Hash::MultiValue.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Hash-MultiValue/LICENSE
