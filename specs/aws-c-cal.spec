Name:           aws-c-cal
Version:        0.5.12 
Release:        2%{?dist}
Summary:        AWS Crypto Abstraction Layer

License:        ASL-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel = 0.6.14
BuildRequires:  openssl-devel

Requires:       aws-c-common-libs = 0.6.14
Requires:       openssl

%description
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for
cryptography primitives


%package libs
Summary:        AWS Crypto Abstraction Layer
Requires:       %{name}%{?_isa} = %{version}-%{release}
	
%description libs
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for
cryptography primitives


%package devel
Summary:        AWS Crypto Abstraction Layer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for
cryptography primitives


%prep
%autosetup


%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install


%files
%license LICENSE
%doc README.md

%{_bindir}/sha256_profile

%files libs
%{_libdir}/libaws-c-cal.so
%{_libdir}/libaws-c-cal.so.1.0.0

%files devel
%{_includedir}/aws/cal/*.h

%{_libdir}/aws-c-cal/cmake/aws-c-cal-config.cmake
%{_libdir}/aws-c-cal/cmake/modules/FindLibCrypto.cmake
%{_libdir}/aws-c-cal/cmake/shared/aws-c-cal-targets-noconfig.cmake
%{_libdir}/aws-c-cal/cmake/shared/aws-c-cal-targets.cmake


%changelog
* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.5.12-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-1
- Initial package development
