%global srcname pbkdf2

Name:           python2-pbkdf2
Version:        1.3
Release:        10%{?dist}
Summary:        A module for a password-based key derivation function

License:        MIT
URL:            https://www.dlitz.net/software/python-pbkdf2/
Source0:        https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel 

%description
A pure Python2 Implementation of the password-based key derivation function,
PBKDF2, specified in RSA PKCS#5 v2.0.

%prep
%autosetup -n %{srcname}-%{version}

find . -type f -name "*.py" -exec sed -i 's#/usr/bin/python#/usr/bin/env python2#g' {} +

%build
%py2_build

%install
%py2_install

%files 
%doc PKG-INFO
%doc README.txt
%{python2_sitelib}/*


%changelog

* Mon Oct 22 2018 David Va <davidva AT tuta DOT io> 1.3-10
- Upstream

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3-6
- Rebuild for Python 3.6

* Tue Nov 08 2016 Jonny Heggheim <jonnyheggheim@sigaint.org> - 1.3-5
- Use autosetup
- Corrrected the LICENSE file to MIT
- Enable tests

* Mon Apr 25 2016 Samuel Gyger <gygers@fsfe.org> - 1.3-4
- Build for python2 and python3
- Use pybuild and pyinstall

* Mon Apr 25 2016 Samuel Gyger <gygers@fsfe.org> - 1.3-3
- Added proper license file and fixed license

* Tue Jan 27 2015 Samuel Gyger <gygers@fsfe.org> - 1.3-2
- Fixed to be only for python2

* Tue Jan 27 2015 Samuel Gyger <gygers@fsfe.org> - 1.3-1
- Created the initial packaging for pkbdf2 on fedora.
