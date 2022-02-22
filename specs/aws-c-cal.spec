Name:           aws-c-cal
Version:        0.5.12 
Release:        5%{?dist}
Summary:        AWS Crypto Abstraction Layer

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-cal-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel = 0.6.14
BuildRequires:  openssl-devel

Requires:       aws-c-common-libs = 0.6.14
Requires:       openssl
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for
cryptography primitives


%package libs
Summary:        AWS Crypto Abstraction Layer

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
%autosetup -p1


%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%files
%{_bindir}/sha256_profile

%files libs
%license LICENSE
%doc README.md
%{_libdir}/libaws-c-cal.so.1.0.0

%files devel
%dir %{_includedir}/aws/cal
%{_includedir}/aws/cal/*.h

%dir %{_libdir}/cmake/aws-c-cal
%dir %{_libdir}/cmake/aws-c-cal/modules
%dir %{_libdir}/cmake/aws-c-cal/shared
%{_libdir}/libaws-c-cal.so
%{_libdir}/cmake/aws-c-cal/aws-c-cal-config.cmake
%{_libdir}/cmake/aws-c-cal/modules/FindLibCrypto.cmake
%{_libdir}/cmake/aws-c-cal/shared/aws-c-cal-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-cal/shared/aws-c-cal-targets.cmake


%changelog
* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-5
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-4
- Move sha256_profile executable to standard package

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.5.12-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-1
- Initial package development
