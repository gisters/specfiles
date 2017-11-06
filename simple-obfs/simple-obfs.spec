%global commit1 3bcb8324431d3bd4be5e4ff2a4323b455c8d5409
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name:			simple-obfs
Version:		0.0.4
Release:		1%{?dist}
Summary:		A simple obfuscating tool

Group:			Applications/Internet
License:		GPLv3+
URL:			https://github.com/shadowsocks/%{name}
Source0:		%{url}/archive/v%{version}.tar.gz
Source1:		https://github.com/shadowsocks/libcork/archive/%{commit1}.tar.gz#/libcork-%{shortcommit1}.tar.gz
AutoReq:		no
BuildRequires:	asciidoc, autoconf, automake, c-ares-devel, gcc, libev-devel, libtool, make, openssl-devel, xmlto, zlib-devel
Requires:		libev, c-ares, openssl, pcre, udns, zlib


%description
Simple-obfs is a simple obfusacting tool, designed as plugin server of shadowsocks.

%prep
%autosetup -n %{name}-%{version} -a 1

rmdir libcork
mv -f libcork-%{commit1} libcork

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_docdir}/*


%changelog
