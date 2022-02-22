Name:           aws-c-auth
Version:        0.6.5 
Release:        5%{?dist}
Summary:        C99 library implementation of AWS client-side authentication

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-auth-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  aws-c-common-devel = 0.6.14
BuildRequires:  aws-c-sdkutils-devel = 0.1.1
BuildRequires:  aws-c-cal-devel = 0.5.12
BuildRequires:  aws-c-io-devel = 0.10.12
BuildRequires:  aws-c-compression-devel = 0.2.14
BuildRequires:  aws-c-http-devel = 0.6.8

Requires:       openssl
Requires:       aws-c-common-libs = 0.6.14
Requires:       aws-c-sdkutils-libs = 0.1.1
Requires:       aws-c-cal-libs = 0.5.12
Requires:       aws-c-io-libs = 0.10.12
Requires:       aws-c-compression-libs = 0.2.14
Requires:       aws-c-http-libs = 0.6.8

%description
C99 library implementation of AWS client-side authentication:
standard credentials providers and signing


%package libs
Summary:        C99 library implementation of AWS client-side authentication

%description libs
C99 library implementation of AWS client-side authentication:
standard credentials providers and signing


%package devel
Summary:        C99 library implementation of AWS client-side authentication
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
C99 library implementation of AWS client-side authentication:
standard credentials providers and signing


%prep
%autosetup -p1


%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install


%files libs
%license LICENSE
%doc README.md
%{_libdir}/libaws-c-auth.so.1.0.0

%files devel
%dir %{_includedir}/aws/auth
%{_includedir}/aws/auth/*.h
%{_libdir}/libaws-c-auth.so
%dir %{_libdir}/cmake/aws-c-auth
%dir %{_libdir}/cmake/aws-c-auth/shared
%{_libdir}/cmake/aws-c-auth/aws-c-auth-config.cmake
%{_libdir}/cmake/aws-c-auth/shared/aws-c-auth-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-auth/shared/aws-c-auth-targets.cmake



%changelog
* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.5-5
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.5-4
- Add patch to set CMake configs to correct path

* Thu Feb 03 2022 David Duncan <davdunc@amazon.com> - 0.6.5-3
- Fix CMake targets and move files to lib

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.6.5-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.5.1
- Initial package development
