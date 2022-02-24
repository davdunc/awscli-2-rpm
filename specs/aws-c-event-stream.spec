Name:           aws-c-event-stream
Version:        0.2.7 
Release:        5%{?dist}
Summary:        C99 implementation of the vnd.amazon.eventstream content-type

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-event-stream-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel = 0.6.14
BuildRequires:  aws-checksums-devel = 0.1.12
BuildRequires:  aws-c-io-devel = 0.10.12

Requires:       aws-c-common-libs = 0.6.14
Requires:       aws-checksums-libs = 0.1.12
Requires:       aws-c-io-libs = 0.10.12

%description
C99 implementation of the vnd.amazon.eventstream content-type


%package libs
Summary:        C99 implementation of the vnd.amazon.eventstream content-type

%description libs
C99 implementation of the vnd.amazon.eventstream content-type


%package devel
Summary:        C99 implementation of the vnd.amazon.eventstream content-type
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
C99 implementation of the vnd.amazon.eventstream content-type


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
%{_libdir}/libaws-c-event-stream.so.1.0.0

%files devel
%dir %{_includedir}/aws/event-stream
%{_includedir}/aws/event-stream/*.h

%dir %{_libdir}/cmake/aws-c-event-stream
%dir %{_libdir}/cmake/aws-c-event-stream/shared
%{_libdir}/libaws-c-event-stream.so
%{_libdir}/cmake/aws-c-event-stream/aws-c-event-stream-config.cmake
%{_libdir}/cmake/aws-c-event-stream/shared/aws-c-event-stream-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-event-stream/shared/aws-c-event-stream-targets.cmake


%changelog
* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 0.2.7-5
- Updated for package review

* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.2.7-4
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.2.7-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.2.7-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.2.7-1
- Build and create package for aws-c-event-stream
