%{?scl:%scl_package nodejs-ansi-regex}
%{!?scl:%global pkg_name %{name}}

%global npm_name ansi-regex

%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:           %{?scl_prefix}nodejs-ansi-regex
Version:        2.0.0
Release:        6%{?dist}
Summary:        Regular expression for matching ANSI escape codes
Url:            https://github.com/sindresorhus/ansi-regex
Source0:        http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:        MIT
BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:	%{?scl_prefix}runtime

%if 0%{?enable_tests}
BuildRequires: %{?scl_prefix}npm(mocha)
%endif

%description
Regular expression for matching ANSI escape codes

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
mocha test/test.js
#node test/viewCodes.js
%endif

%files
%{nodejs_sitelib}/ansi-regex

%doc readme.md license

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-6
- rh-nodejs8 rebuild

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-5
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-4
- Rebuilt with updated metapackage

* Mon Dec 14 2015 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-2
- Enable scl macros

* Mon Sep 14 2015 Troy Dawson <tdawson@redhat.com> - 2.0.0-4
- UPdate to 2.1.0
- Remove tests until all dependencies are built

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.1-1
- Initial build
