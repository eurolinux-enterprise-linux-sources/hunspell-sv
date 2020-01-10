Name: hunspell-sv
Summary: Swedish hunspell dictionaries
Version: 2.10
Release: 3%{?dist}
Source: http://dsso.googlecode.com/files/sv-%{version}.zip
Group: Applications/Text
URL: http://dsso.se/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv3
BuildArch: noarch

Requires: hunspell

%description
Swedish hunspell dictionaries.

%prep
%setup -q -c -n hunspell-sv

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.txt

%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.10-3
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Caolán McNamara <caolanm@redhat.com> - 2.10-1
- Resolves: rhbz#868507 latest version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 08 2011 Caolán McNamara <caolanm@redhat.com> - 1.48-1
- latest version

* Wed Nov 16 2011 Caolán McNamara <caolanm@redhat.com> - 1.47-1
- latest version

* Wed Jun 29 2011 Caolán McNamara <caolanm@redhat.com> - 1.46-1
- latest version

* Thu Jun 09 2011 Caolán McNamara <caolanm@redhat.com> - 1.45-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Caolán McNamara <caolanm@redhat.com> - 1.44-1
- latest version

* Mon Jul 05 2010 Caolán McNamara <caolanm@redhat.com> - 1.43-1
- latest version

* Wed Apr 07 2010 Caolán McNamara <caolanm@redhat.com> - 1.42-2
- clarify licence

* Tue Feb 02 2010 Caolán McNamara <caolanm@redhat.com> - 1.42-1
- latest version

* Thu Jan 14 2010 Caolán McNamara <caolanm@redhat.com> - 1.41-1
- latest version

* Tue Nov 17 2009 Caolán McNamara <caolanm@redhat.com> - 1.40-2
- prefer .zip

* Tue Nov 03 2009 Caolán McNamara <caolanm@redhat.com> - 1.40-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 14 2009 Caolán McNamara <caolanm@redhat.com> - 1.39-1
- latest version

* Thu Jun 04 2009 Caolán McNamara <caolanm@redhat.com> - 1.38-1
- latest version

* Mon Jun 01 2009 Caolán McNamara <caolanm@redhat.com> - 1.37-1
- latest version

* Tue May 26 2009 Caolán McNamara <caolanm@redhat.com> - 1.35-1
- latest version

* Fri May 22 2009 Caolán McNamara <caolanm@redhat.com> - 1.33-1
- latest version

* Tue May 19 2009 Caolán McNamara <caolanm@redhat.com> - 1.32-1
- latest version

* Mon May 11 2009 Caolán McNamara <caolanm@redhat.com> - 1.31-1
- latest version

* Mon Apr 13 2009 Caolán McNamara <caolanm@redhat.com> - 1.30-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 23 2008 Caolán McNamara <caolanm@redhat.com> - 1.29-1
- latest version
`
* Tue Jun 17 2008 Caolán McNamara <caolanm@redhat.com> - 1.28-1
- latest version

* Wed May 28 2008 Caolán McNamara <caolanm@redhat.com> - 1.27-1
- latest version

* Thu May 13 2008 Caolán McNamara <caolanm@redhat.com> - 1.26-1
- latest version

* Thu Mar 13 2008 Caolán McNamara <caolanm@redhat.com> - 1.25-1
- latest version

* Wed Mar 05 2008 Caolán McNamara <caolanm@redhat.com> - 1.23-1
- latest version

* Fri Aug 03 2007 Caolán McNamara <caolanm@redhat.com> - 1.22-2
- clarify license version

* Fri Jul 06 2007 Caolán McNamara <caolanm@redhat.com> - 1.22-1
- move to dsso.se dictionaries

* Fri Jul 06 2007 Caolán McNamara <caolanm@redhat.com> - 1.3.8.6b-1
- latest version

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 1.3.8.6-1
- initial version
