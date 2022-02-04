%global srcname aws-cli
%global appname awscli

Name:           %{appname}-2
Version:        2.4.12
Release:        3%{?dist}
Summary:        Universal Command Line Environment for AWS, Version 2

License:        ASL 2.0 and MIT
URL:            https://github.com/aws/aws-cli
Source0:        %{url}/archive/%{version}/%{appname}-%{version}.tar.gz
Patch0:         awscli-2.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)

Recommends:     groff
Obsoletes:      awscli <= 1
Obsoletes:      python3-botocore <= 1


%description

This package provides version 2 of the unified command line
interface to Amazon Web Services.


%prep
%autosetup -p1 -n %{srcname}-%{version}
find awscli/examples/ -type f -name '*.rst' -executable -exec chmod -x '{}' +

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files awscli


%check
# The test command ignores two files because they import
# jsonschema which is not able to be imported via the pytest
# runner. It is similar to this issue: https://github.com/Julian/jsonschema/issues/584
# This should be only temporary as once jsonschema is updated to the latest
# version in Fedora, pytest is able to properly import it.
%pytest tests/unit tests/functional --ignore=tests/functional/botocore/test_waiter_config.py --ignore=tests/functional/autocomplete/test_completion_files.py


%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%{_bindir}/aws
%{_bindir}/aws.cmd
%{_bindir}/aws_bash_completer
%{_bindir}/aws_completer
%{_bindir}/aws_zsh_completer.sh


%changelog
* Fri Feb 04 2022 Kyle Knapp <kyleknap@amazon.com> - 2.4.12-3
- Remove unneeded dependencies/macros and add check for tests

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 2.4.12-2
- Prepare for package review

* Tue Jan 25 2022 Kyle Knapp <kyleknap@amazon.com> - 2.4.12-1
- Update to 2.4.12 and switch to using pyproject macros

* Fri Mar 13 2020 David Duncan <davdunc@amazon.com> - 2.0.3-2
- Modify python3-botocore dependency to python3-botocore-2

* Fri Mar 13 2020 David Duncan <davdunc@amazon.com> - 2.0.3-1
- Initial Commit for awscli version 2
