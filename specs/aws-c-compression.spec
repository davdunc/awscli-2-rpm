Name:           aws-c-compression
Version:        0.2.14
Release:        2%{?dist}
Summary:        Compression package for AWS SDK for C

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel = 0.6.14

Requires:       aws-c-common-libs = 0.6.14

%description
This is a cross-platform C99 implementation of
compression algorithms such as gzip, and huffman encoding/decoding.


%package libs
Summary:        Compression package for AWS SDK for C
Requires:       %{name}%{?_isa} = %{version}-%{release}
	
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
%{_libdir}/libaws-c-compression.so
%{_libdir}/libaws-c-compression.so.1.0.0

%files devel
%{_includedir}/aws/compression/*.h

%{_libdir}/aws-c-compression/cmake/aws-c-compression-config.cmake
%{_libdir}/aws-c-compression/cmake/shared/aws-c-compression-targets-noconfig.cmake
%{_libdir}/aws-c-compression/cmake/shared/aws-c-compression-targets.cmake


%changelog
* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.2.14-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.2.14-1
- Initial pacakage development
