Name:           aws-c-event-stream
Version:        0.2.7 
Release:        2%{?dist}
Summary:        C99 implementation of the vnd.amazon.eventstream content-type

License:        ASL-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

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
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description libs
C99 implementation of the vnd.amazon.eventstream content-type


%package devel
Summary:        C99 implementation of the vnd.amazon.eventstream content-type
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
C99 implementation of the vnd.amazon.eventstream content-type


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
%{_libdir}/libaws-c-event-stream.so
%{_libdir}/libaws-c-event-stream.so.1.0.0

%files devel
%{_includedir}/aws/event-stream/*.h

%{_libdir}/aws-c-event-stream/cmake/aws-c-event-stream-config.cmake
%{_libdir}/aws-c-event-stream/cmake/shared/aws-c-event-stream-targets-noconfig.cmake
%{_libdir}/aws-c-event-stream/cmake/shared/aws-c-event-stream-targets.cmake


%changelog
* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.2.7-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.2.7-1
- Build and create package for aws-c-event-stream
