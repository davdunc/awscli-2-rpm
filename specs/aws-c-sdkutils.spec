Name:           aws-c-sdkutils
Version:        0.1.1 
Release:        4%{?dist}
Summary:        Utility package for AWS SDK for C

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-sdkutils-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel = 0.6.14

Requires:       aws-c-common-libs = 0.6.14

%description
Utility package for AWS SDK for C


%package libs
Summary:        Utility package for AWS SDK for C

%description libs
Utility package for AWS SDK for C


%package devel
Summary:        Utility package for AWS SDK for C
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Utility package for AWS SDK for C


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
%{_libdir}/libaws-c-sdkutils.so.1.0.0

%files devel
%dir %{_includedir}/aws/sdkutils
%{_includedir}/aws/sdkutils/*.h

%dir %{_libdir}/cmake/aws-c-sdkutils
%dir %{_libdir}/cmake/aws-c-sdkutils/shared
%{_libdir}/libaws-c-sdkutils.so
%{_libdir}/cmake/aws-c-sdkutils/aws-c-sdkutils-config.cmake
%{_libdir}/cmake/aws-c-sdkutils/shared/aws-c-sdkutils-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-sdkutils/shared/aws-c-sdkutils-targets.cmake


%changelog
* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.1-4
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.1-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.1.1-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.1-1
- Initial package development
