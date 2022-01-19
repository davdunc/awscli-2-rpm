Name:           aws-c-sdkutils
Version:        0.1.1 
Release:        1%{?dist}
Summary:        Utility package for AWS SDK for C
Epoch:          1

License:        ASL-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel

Requires:       aws-c-common-libs

%description
Utility package for AWS SDK for C


%package libs
Summary:        Utility package for AWS SDK for C
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
	
%description libs
Utility package for AWS SDK for C


%package devel
Summary:        Utility package for AWS SDK for C
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Utility package for AWS SDK for C


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
%{_libdir}/libaws-c-sdkutils.so
%{_libdir}/libaws-c-sdkutils.so.1.0.0

%files devel
%{_includedir}/aws/sdkutils/*.h

%{_libdir}/aws-c-sdkutils/cmake/aws-c-sdkutils-config.cmake
%{_libdir}/aws-c-sdkutils/cmake/shared/aws-c-sdkutils-targets-noconfig.cmake
%{_libdir}/aws-c-sdkutils/cmake/shared/aws-c-sdkutils-targets.cmake


%changelog
* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com>
- 
