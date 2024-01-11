Name: openoffice.org-dict-cs_CZ
Version: 20080822
Release: 8%{?dist}
Summary: Czech spellchecker and hyphenation dictionaries for LibreOffice
License: GPL+
URL: http://extensions.services.openoffice.org/en/project/dict-cs
Source0: http://downloads.sourceforge.net/aoo-extensions/dict-cs-2.0.oxt
BuildArch: noarch

BuildRequires: dos2unix

# rhbz#1173776
Patch0: cs_CZ.aff.patch

%global hunspelldir %{_datadir}/myspell
%global hyphendir %{_datadir}/hyphen

%description
This package contains the Czech hyphenation dictionaries for the LibreOffice
application suite.

%package -n hunspell-cs
Summary: Czech hunspell dictionary
Requires: hunspell
Obsoletes: openoffice.org-dict-cs_CZ < %{version}-%{release}

%description -n hunspell-cs
This package contains the Czech dictionary for the hunspell spellchecker.

%package -n hyphen-cs
Summary: Czech hyphenation rules
Requires: hyphen
Obsoletes: openoffice.org-dict-cs_CZ < %{version}-%{release}

%description -n hyphen-cs
Czech hyphenation rules.

%prep
%setup -q -c -n %{name}
%patch0 -p4
dos2unix README_*.txt

%build

%install
mkdir -p $RPM_BUILD_ROOT%{hunspelldir}
install -m 644 cs* $RPM_BUILD_ROOT%{hunspelldir}
mkdir -p $RPM_BUILD_ROOT%{hyphendir}
install -m 644 hyph*.dic $RPM_BUILD_ROOT%{hyphendir}

%files -n hyphen-cs
%doc README_cs.txt README_en.txt
%{hyphendir}/hyph_cs*

%files -n hunspell-cs
%doc README_cs.txt README_en.txt
%{hunspelldir}/cs*

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20080822-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080822-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080822-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20080822-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080822-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 15 2014 David Tardon <dtardon@redhat.com> - 20080822-3
- Resolves: rhbz#1173776 fix syntax of .aff file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080822-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 David Tardon <dtardon@redhat.com> - 20080822-1
- update to a new version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060303-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 26 2007 Tomas Mraz <tmraz@redhat.com> - 20060303-7
- add obsoletes openoffice.org-dict-cs_CZ

* Mon Nov 26 2007 Caolan McNamara <caolanm@redhat.com> - 20060303-6
- Resolves: rhbz#398361 move hyphenation rules into hyphen dir where OOo will now autodetect them

* Tue Mar 27 2007 Tomas Mraz <tmraz@redhat.com> - 20060303-5
- add hunspell-cs subpackage (#232416)
- openoffice datadir moved again

* Mon Jan 29 2007 Tomas Mraz <tmraz@redhat.com> - 20060303-4
- disable useless debuginfo (#225094)

* Mon Dec 11 2006 Tomas Mraz <tmraz@redhat.com> - 20060303-3
- package must be arch-specific now because ooo is now 64bit on x86_64 as
  well (#219100)

* Thu Sep  7 2006 Tomas Mraz <tmraz@redhat.com> - 20060303-2
- rebuilt for FC6

* Mon Mar 21 2005 Tomas Mraz <tmraz@redhat.com> - 20060303-1
- Initial package
