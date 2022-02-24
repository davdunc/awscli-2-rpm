Name:           aws-c-compression
Version:        0.2.14
Release:        5%{?dist}
Summary:        Compression package for AWS SDK for C

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-compression-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel = 0.6.14

Requires:       aws-c-common-libs = 0.6.14

%description
This is a cross-platform C99 implementation of
compression algorithms such as gzip, and huffman encoding/decoding.


%package libs
Summary:        Compression package for AWS SDK for C

%description libs
This is a cross-platform C99 implementation of
compression algorithms such as gzip, and huffman encoding/decoding.


%package devel
Summary:        Compression package for AWS SDK for C
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This is a cross-platform C99 implementation of
compression algorithms such as gzip, and huffman encoding/decoding.


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
%{_libdir}/libaws-c-compression.so.1.0.0

%files devel
%dir %{_includedir}/aws/compression
%{_includedir}/aws/compression/*.h

%dir %{_libdir}/cmake/aws-c-compression
%dir %{_libdir}/cmake/aws-c-compression/shared
%{_libdir}/libaws-c-compression.so
%{_libdir}/cmake/aws-c-compression/aws-c-compression-config.cmake
%{_libdir}/cmake/aws-c-compression/shared/aws-c-compression-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-compression/shared/aws-c-compression-targets.cmake


%changelog
* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 0.2.14-5
- Updated for package review

* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.2.14-4
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.2.14-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.2.14-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.2.14-1
- Initial pacakage development
