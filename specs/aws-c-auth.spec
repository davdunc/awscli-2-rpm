Name:           aws-c-auth
Version:        0.6.5 
Release:        1%{?dist}
Summary:        C99 library implementation of AWS client-side authentication

License:        ASL-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  aws-c-common-devel = 1:0.6.14
BuildRequires:  aws-c-sdkutils-devel = 1:0.1.1
BuildRequires:  aws-c-cal-devel = 1:0.5.12
BuildRequires:  aws-c-io-devel = 1:0.10.12
BuildRequires:  aws-c-compression-devel = 1:0.2.14
BuildRequires:  aws-c-http-devel = 1:0.6.8

Requires:       openssl
Requires:       aws-c-common-libs = 1:0.6.14
Requires:       aws-c-sdkutils-libs = 1:0.1.1
Requires:       aws-c-cal-libs = 1:0.5.12
Requires:       aws-c-io-libs = 1:0.10.12
Requires:       aws-c-compression-libs = 1:0.2.14
Requires:       aws-c-http-libs = 1:0.6.8

%description
C99 library implementation of AWS client-side authentication:
standard credentials providers and signing


%package libs
Summary:        C99 library implementation of AWS client-side authentication
Requires:       %{name}%{?_isa} = %{version}-%{release}

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
%autosetup


%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install


%files
%license LICENSE
%doc README.md

%files libs
%{_libdir}/libaws-c-auth.so
%{_libdir}/libaws-c-auth.so.1.0.0

%files devel
%{_includedir}/aws/auth/*.h

%{_libdir}/aws-c-auth/cmake/aws-c-auth-config.cmake
%{_libdir}/aws-c-auth/cmake/shared/aws-c-auth-targets-noconfig.cmake
%{_libdir}/aws-c-auth/cmake/shared/aws-c-auth-targets.cmake



%changelog
* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com>
- 
