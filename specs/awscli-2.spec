%global srcname aws-cli
%global appname awscli

%bcond_with examples

Name:           %{appname}-2
Version:        2.4.12
Release:        1%{?dist}
Summary:        Universal Command Line Environment for AWS, Version 2

License:        ASL 2.0 and MIT
URL:            https://github.com/aws/aws-cli
Source0:        %{url}/archive/%{version}/%{appname}-%{version}.tar.gz
Patch0:         awscli-2.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-toml
BuildRequires:  python3-wheel

Recommends:     groff
Obsoletes:      awscli <= 1
Obsoletes:      python3-botocore <= 1

%{?python_provide:%python_provide python3-%{name}}

%description

This package provides version 2 of the unified command line
interface to Amazon Web Services.


%prep
%autosetup -p1 -n %{srcname}-%{version}

%if %{with examples}
find awscli/examples/ -type f -name '*.rst' -executable -exec chmod -x '{}' +
%else
rm -r awscli/examples
%endif

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files awscli

%files -f %{pyproject_files}
%doc README.rst

%{_bindir}/aws
%{_bindir}/aws.cmd
%{_bindir}/aws_bash_completer
%{_bindir}/aws_completer
%{_bindir}/aws_zsh_completer.sh


%changelog
* Fri Mar 13 2020 David Duncan <davdunc@amazon.com> - 2.0.3-2
- Modify python3-botocore dependency to python3-botocore-2

* Fri Mar 13 2020 David Duncan <davdunc@amazon.com> - 2.0.3-1
- Initial Commit for awscli version 2
