Name:           aws-c-s3
Version:        0.1.27
Release:        4%{?dist}
Summary:        C99 library implementation for communicating with the S3 service

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-s3-cmake.patch

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
%autosetup -p1


%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install


%files libs
%license LICENSE
%doc README.md
%{_libdir}/libaws-c-s3.so.0unstable
%{_libdir}/libaws-c-s3.so.1.0.0

%files devel
%dir %{_includedir}/aws/s3
%{_includedir}/aws/s3/*.h

%dir %{_libdir}/cmake/aws-c-s3
%dir %{_libdir}/cmake/aws-c-s3/shared
%{_libdir}/libaws-c-s3.so
%{_libdir}/cmake/aws-c-s3/aws-c-s3-config.cmake
%{_libdir}/cmake/aws-c-s3/shared/aws-c-s3-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-s3/shared/aws-c-s3-targets.cmake



%changelog
* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.27-4
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.27-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.1.27-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.27-1
- Initial package development
