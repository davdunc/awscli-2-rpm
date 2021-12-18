Name:           s2n-tls
Version:        1.3.2
Release:        1%{?dist}
Summary:        s2n: an implementation of the TLS/SSL protocols

License:        ASL-2.0
URL:            https://github.com/davdunc/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: openssl-devel
BuildRequires: ninja-build
Requires:      openssl

%description
s2n-tls is a C99 implementation of the TLS/SSL protocols that is
designed to be simple, small, fast, and with security as a priority.

%prep
%autosetup


%build
%cmake
%cmake_build

%install
%cmake_install


%files
%license LICENSE
%doc VERSIONING.rst NOTICE README.md
%doc docs/READING-LIST.md docs/USAGE-GUIDE.md



%changelog
* Sat Dec 18 2021 David Duncan <<davdunc@amazon.com>>
- 
