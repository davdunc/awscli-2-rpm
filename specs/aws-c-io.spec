Name:           aws-c-io
Version:        0.10.12 
Release:        3%{?dist}
Summary:        IO package for AWS SDK for C

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-io-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  s2n-tls-devel
BuildRequires:  aws-c-common-devel = 0.6.14
BuildRequires:  aws-c-cal-devel = 0.5.12

Requires:       s2n-tls-libs
Requires:       aws-c-common-libs = 0.6.14
Requires:       aws-c-cal-libs = 0.5.12

%description
IO package for AWS SDK for C. It handles all IO and TLS work
for application protocols.


%package libs
Summary:        IO package for AWS SDK for C

%description libs
IO package for AWS SDK for C. It handles all IO and TLS work
for application protocols.


%package devel
Summary:        IO package for AWS SDK for C
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       s2n-tls-devel
Requires:       aws-c-cal-devel = 0.5.12

%description devel
IO package for AWS SDK for C. It handles all IO and TLS work
for application protocols.


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
%{_libdir}/libaws-c-io.so.1.0.0

%files devel
%{_includedir}/aws/io/*.h
%{_includedir}/aws/testing/io_testing_channel.h

%{_libdir}/libaws-c-io.so
%{_libdir}/cmake/aws-c-io/aws-c-io-config.cmake
%{_libdir}/cmake/aws-c-io/shared/aws-c-io-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-io/shared/aws-c-io-targets.cmake


%changelog
* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.10.12-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.10.12-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.10.12-1
- Initial package development 
