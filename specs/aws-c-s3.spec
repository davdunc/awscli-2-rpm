Name:           aws-c-s3
Version:        0.1.27
Release:        1%{?dist}
Summary:        C99 library implementation for communicating with the S3 service

License:        ASL-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel = 0.6.14
BuildRequires:  aws-c-sdkutils-devel = 0.1.1
BuildRequires:  aws-c-cal-devel = 0.5.12
BuildRequires:  aws-c-compression-devel = 0.2.14
BuildRequires:  aws-c-io-devel = 0.10.12
BuildRequires:  aws-c-http-devel = 0.6.8
BuildRequires:  aws-c-auth-devel = 0.6.5

Requires:       aws-c-common-libs = 0.6.14
Requires:       aws-c-sdkutils-libs = 0.1.1
Requires:       aws-c-cal-libs = 0.5.12
Requires:       aws-c-compression-libs = 0.2.14
Requires:       aws-c-io-libs = 0.10.12
Requires:       aws-c-http-libs = 0.6.8
Requires:       aws-c-auth-libs = 0.6.5

%description
C99 library implementation for communicating with the S3 service,
designed for maximizing throughput on high bandwidth EC2 instances.

%package libs
Summary:        C99 library implementation for communicating with the S3 service
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description libs
C99 library implementation for communicating with the S3 service,
designed for maximizing throughput on high bandwidth EC2 instances.


%package devel
Summary:        C99 library implementation for communicating with the S3 service
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
C99 library implementation for communicating with the S3 service,
designed for maximizing throughput on high bandwidth EC2 instances.


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
%{_libdir}/libaws-c-s3.so
%{_libdir}/libaws-c-s3.so.0unstable
%{_libdir}/libaws-c-s3.so.1.0.0

%files devel
%{_includedir}/aws/s3/*.h

%{_libdir}/aws-c-s3/cmake/aws-c-s3-config.cmake
%{_libdir}/aws-c-s3/cmake/shared/aws-c-s3-targets-noconfig.cmake
%{_libdir}/aws-c-s3/cmake/shared/aws-c-s3-targets.cmake



%changelog
* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com>
- 
