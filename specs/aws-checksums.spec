Name:           aws-checksums
Version:        0.1.12 
Release:        4%{?dist}
Summary:        Checksum package for AWS SDK for C

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-checksums-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel = 0.6.14

Requires:       aws-c-common-libs = 0.6.14

%description
Checksum package for AWS SDK for C. Contains
Cross-Platform HW accelerated CRC32c and CRC32 with
fallback to efficient SW implementations.


%package libs
Summary:        Checksum package for AWS SDK for C

%description libs
Checksum package for AWS SDK for C. Contains
Cross-Platform HW accelerated CRC32c and CRC32 with
fallback to efficient SW implementations.


%package devel
Summary:        Checksum package for AWS SDK for C
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Checksum package for AWS SDK for C. Contains
Cross-Platform HW accelerated CRC32c and CRC32 with
fallback to efficient SW implementations.


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
%{_libdir}/libaws-checksums.so.1.0.0

%files devel
%dir %{_includedir}/aws/checksums
%{_includedir}/aws/checksums/*.h

%dir %{_libdir}/cmake/aws-checksums
%dir %{_libdir}/cmake/aws-checksums/shared
%{_libdir}/libaws-checksums.so
%{_libdir}/cmake/aws-checksums/aws-checksums-config.cmake
%{_libdir}/cmake/aws-checksums/shared/aws-checksums-targets-noconfig.cmake
%{_libdir}/cmake/aws-checksums/shared/aws-checksums-targets.cmake


%changelog
* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.12-4
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.12-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.1.12-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.12-1
- Initial package development
