%global commit 1e5b3780468cadb1b3efa456434b525c208c888d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global v2ray_ver 4.16.0
%define debug_package %{nil}

Name:           v2ray-plugin
Version:        1.1.0
Release:        1%{?dist}
Summary:        A SIP003 plugin based on v2ray

Group:          Network
License:        MIT
URL:            https://github.com/shadowsocks/v2ray-plugin
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        https://github.com/v2ray/v2ray-core/releases/download/v%{v2ray_ver}/src_all.zip

BuildRequires:  git golang

%description
Yet another SIP003 plugin for shadowsocks, based on v2ray

%prep
rm -rf %{name}-%{version}
%setup -c -T -D -a 0 -a 1
mkdir -p ./_build
ln -s $(pwd) ./_build/src


%build
export GOPATH=$(pwd)/_build
cd %{name}-%{commit}
export LDFLAGS="-X main.VERSION=%{version}"
CGO_ENABLED=0 go build -v -ldflags "$LDFLAGS" -gcflags "" -o _bin/v2ray-plugin

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{name}-%{commit}/_bin/v2ray-plugin %{buildroot}%{_bindir}

%files
%{_bindir}/v2ray-plugin

%changelog
