Name:           aws-c-event-stream
Version:        0.2.7 
Release:        1%{?dist}
Summary:        C99 implementation of the vnd.amazon.eventstream content-type
Epoch:          1

License:        ASL-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel = 1:0.6.14
BuildRequires:  aws-checksums-devel = 1:0.1.12
BuildRequires:  aws-c-io-devel = 1:0.10.12

Requires:       aws-c-common-libs = 1:0.6.14
Requires:       aws-checksums-libs = 1:0.1.12
Requires:       aws-c-io-libs = 1:0.10.12

%description
C99 implementation of the vnd.amazon.eventstream content-type


%package libs
Summary:        C99 implementation of the vnd.amazon.eventstream content-type
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description libs
C99 implementation of the vnd.amazon.eventstream content-type


%package devel
Summary:        C99 implementation of the vnd.amazon.eventstream content-type
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

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
* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com>
- 
