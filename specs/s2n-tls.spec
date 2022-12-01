Name:           s2n-tls
Version:        1.3.29
Release:        1%{?dist}
Summary:        s2n: an implementation of the TLS/SSL protocols utilities

License:        ASL 2.0
URL:            https://github.com/aws/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: openssl-devel
BuildRequires: ninja-build
Requires:      openssl

%description
s2n-tls is a C99 implementation of the TLS/SSL protocols that is
designed to be simple, small, fast, and with security as a priority.

%package libs
Summary: s2n: an implementation of the TLS/SSL protocols libraries
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description libs 
s2n-tls is a C99 implementation of the TLS/SSL protocols that is
designed to be simple, small, fast, and with security as a priority.

%package devel
Summary: s2n: an implementation of the TLS/SSL protocols headers and source files.
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Requires:      openssl-devel

%description devel
Headers and Source files for s2n-tls is a C99 implementation of the
TLS/SSL protocols that is designed to be simple, small, fast, and with
security as a priority.

%prep
%autosetup


%build
%cmake -DUNSAFE_TREAT_WARNINGS_AS_ERRORS=OFF -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install


%files devel
%{_includedir}/s2n.h
%{_libdir}/s2n/cmake/modules/FindLibCrypto.cmake
%{_libdir}/s2n/cmake/s2n-config.cmake
%{_libdir}/s2n/cmake/shared/s2n-targets-noconfig.cmake
%{_libdir}/s2n/cmake/shared/s2n-targets.cmake


%files libs
%license LICENSE
%{_libdir}/libs2n.so

%files
%license LICENSE
%doc VERSIONING.rst NOTICE README.md
%doc docs/READING-LIST.md docs/USAGE-GUIDE.md



%changelog
* Thu Dec 01 2022 David Duncan <davdunc@amazon.com> - 1.3.29-1
- 1.3.29
- Try to clarify the use of s2n_blob_zeroize_free by @lrstewart in GH#3591
- Apache renegotiation integration tests by @goatgoose in GH#3580
- 1.3.27 rust bindings update by @maddeleine in GH#3599
- Add some redundant null ptr validation for defence in depth by @harrisonkaiser in GH#3596
- [bindings] Fix client hello callback with config swap by @lrstewart in GH#3600
- Re-enable saw proofs for TLS handshake with NPN extension disabled by @pennyannn in GH#3594
- Move CRL timestamp validation into the CRL lookup callback by @goatgoose in GH#3515
- Fix to handle callback failure by @aditishri18 in GH#3597
- Adds s2n_connection section to usage guide by @maddeleine in GH#3605
- Fix very minor DeprecationWarning in integrationv2 by @harrisonkaiser in GH#3609
- wrapper for wall_clock by @aditishri18 in GH#3611
- bindings(rust): add lto in release mode by @camshaft in GH#3610

* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 1.3.2-3
- Updated for package review

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 1.3.2-2
- Prepare for package review

* Sat Dec 18 2021 David Duncan <davdunc@amazon.com> - 1.3.2-1
- Initial Package Review release
