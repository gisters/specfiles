Name:           v2ray-plugin
Version:        1.1.0
Release:        1%{?dist}
Summary:        A SIP003 plugin based on v2ray

Group:          Network
License:        MIT
URL:            https://github.com/shadowsocks/v2ray-plugin
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  git >= 1.8.3.1
BuildRequires:  go-compilers-golang-compiler

%description
Yet another SIP003 plugin for shadowsocks, based on v2ray

%prep
rm -rf %{name}-%{version}
%setup -q -D -T -c -n %{name}-%{version} -a 0
export GOPATH=$(pwd)/_build
cd %{name}-%{version}
go mod download

%build
cd %{name}-%{version}
export LDFLAGS="-X main.VERSION=%{version}"
%gobuild -o _bin/v2ray-plugin

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{name}-%{version}/_bin/v2ray-plugin %{buildroot}%{_bindir}

%files
%license %{name}-%{version}/LICENSE
%doc %{name}-%{version}/README.md
%{_bindir}/v2ray-plugin

%changelog
