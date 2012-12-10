%undefine __find_provides
%undefine __find_requires

Summary:	English sound files for the Asterisk PBX and telephony application and toolkit
Name:		asterisk-core-sounds-en
Version:	1.4.22
Release:	%mkrel 1
License:	Public Domain
Group:		System/Servers
URL:		http://www.asterisk.org/
#for FMT in alaw g722 g729 gsm sln16 ulaw wav siren7 siren14; do wget -P SOURCES/ -c http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-core-sounds-fr-${FMT}-1.4.17.tar.gz ; done
Source0:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-alaw-%{version}.tar.gz
Source1:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-g722-%{version}.tar.gz
Source2:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-g729-%{version}.tar.gz
Source3:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-gsm-%{version}.tar.gz
Source4:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-siren7-%{version}.tar.gz
Source5:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-siren14-%{version}.tar.gz
Source6:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-sln16-%{version}.tar.gz
Source7:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-ulaw-%{version}.tar.gz
Source8:	http://downloads.asterisk.org/pub/telephony/sounds/releases/%{name}-wav-%{version}.tar.gz
Requires:	asterisk
Provides:	asterisk-core-sounds = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Asterisk is an Open Source PBX and telephony development platform that can both
replace a conventional PBX and act as a platform for developing custom
telephony applications for delivering dynamic content over a telephone
similarly to how one can deliver dynamic content through a web browser using
CGI and a web server.
 
Asterisk talks to a variety of telephony hardware including BRI, PRI, POTS, and
IP telephony clients using the Inter-Asterisk eXchange protocol (e.g. gnophone
or miniphone).

This package contains freely usable recorded sounds that were meant to be used
with Asterisk in the following formats: a-Law, G.722, G.729, GSM, Siren7, 
Siren14, sln16, mu-Law, WAV

%prep

%setup -q -c -T -n asterisk-core-sounds-%{version} -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8

# fix dir perms
find . -type d | xargs chmod 755
    
# fix file perms
find . -type f | xargs chmod 644

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}/var/lib/asterisk/sounds/en

cp -aRf * %{buildroot}/var/lib/asterisk/sounds/en

# cleanup
#rm -f %{buildroot}%{_datadir}/asterisk/sounds/*-asterisk-core-*-%{version}

# make a file list
find %{buildroot}/var/lib/asterisk/sounds/en -type f | sed -e "s|%{buildroot}||" | sed -e 's/^/%attr(0644,root,root) /' >> %{name}.filelist

%clean
rm -rf %{buildroot}

%files -f %{name}.filelist
%defattr(-,root, root)
%doc *-asterisk-core-*-%{version}


%changelog
* Tue Jul 12 2011 Lonyai Gergely <aleph@mandriva.org> 1.4.22-1mdv2011
+ Revision: 689669
- 1.4.22

* Fri Jun 03 2011 Lonyai Gergely <aleph@mandriva.org> 1.4.21-1
+ Revision: 682572
- 1.4.21

* Fri Oct 22 2010 Lonyai Gergely <aleph@mandriva.org> 1.4.20-1mdv2011.0
+ Revision: 587278
- 1.4.20

* Sat Jul 10 2010 Lonyai Gergely <aleph@mandriva.org> 1.4.19-1mdv2011.0
+ Revision: 550212
- 1.4.19
- Add download comment
  Add version to the Provides

* Wed Jan 06 2010 Lonyai Gergely <aleph@mandriva.org> 1.4.17-1mdv2010.1
+ Revision: 486630
- 1.4.17 files
- 1.4.17

* Fri Oct 09 2009 Lonyai Gergely <aleph@mandriva.org> 1.4.16-1mdv2010.1
+ Revision: 456274
- 1.4.16

* Thu Aug 13 2009 Lonyai Gergely <aleph@mandriva.org> 1.4.15-2mdv2010.0
+ Revision: 416104
- mv all files the en/ subdirectory

* Mon Mar 30 2009 Lonyai Gergely <aleph@mandriva.org> 1.4.15-1mdv2009.1
+ Revision: 362478
- Update: 1.4.15

* Tue Mar 17 2009 Lonyai Gergely <aleph@mandriva.org> 1.4.14-2mdv2009.1
+ Revision: 356990
- sterisk-core-sounds-en-1.4.14-2mdv2009.1

* Thu Feb 19 2009 Lonyai Gergely <aleph@mandriva.org> 1.4.14-1mdv2009.1
+ Revision: 342998
- asterisk-core-sounds-en-1.4.14-1mdv2009.1

* Thu Dec 11 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.13-2mdv2009.1
+ Revision: 313458
- adjust path for asterisk 1.6.x

* Tue Oct 14 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.13-1mdv2009.1
+ Revision: 293636
- 1.4.13

* Thu Aug 14 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.12-1mdv2009.0
+ Revision: 271935
- 1.4.12

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.4.11-2mdv2009.0
+ Revision: 266187
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Wed Apr 09 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.11-1mdv2009.0
+ Revision: 192508
- 1.4.11

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 10 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.5-2mdv2008.0
+ Revision: 84043
- rebuild


* Thu Feb 15 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.5-1mdv2007.0
+ Revision: 121441
- Import asterisk-core-sounds-en

* Thu Feb 15 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.5-1mdv2007.1
- initial Mandriva package

