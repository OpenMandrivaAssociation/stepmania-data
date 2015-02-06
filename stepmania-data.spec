%define gamename StepMania
%define distname %{gamename}-data
%define	name	stepmania-data
%define	version	3.9
%define release	8

Summary:	A rythm game : data files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Url:		http://www.stepmania.com/wiki/Downloads
Group:		Games/Arcade
Source0:	%{distname}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:  	noarch

%description
StepMania is a free dance and rhythm game for Linux. It features 3D 
graphics, keyboard and "dance pad" support, and an editor for creating 
your own steps.

%prep
%setup -q -n %{distname}-%{version}

%install
rm -rf %buildroot
install -d -m 0755 $RPM_BUILD_ROOT/%{_gamesdatadir}/%{gamename}/
cp -a %{_topdir}/BUILD/%{distname}-%{version}/* $RPM_BUILD_ROOT/%{_gamesdatadir}/%{gamename}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{gamename}/Announcers
%{_gamesdatadir}/%{gamename}/BGAnimations
%{_gamesdatadir}/%{gamename}/CDTitles
%{_gamesdatadir}/%{gamename}/Characters
%{_gamesdatadir}/%{gamename}/Courses
%{_gamesdatadir}/%{gamename}/Data
%{_gamesdatadir}/%{gamename}/Docs
%{_gamesdatadir}/%{gamename}/NoteSkins
%{_gamesdatadir}/%{gamename}/RandomMovies
%{_gamesdatadir}/%{gamename}/Songs
%{_gamesdatadir}/%{gamename}/Themes
%{_gamesdatadir}/%{gamename}/Visualizations



%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.9-7mdv2010.0
+ Revision: 445235
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.9-6mdv2009.0
+ Revision: 261176
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.9-5mdv2009.0
+ Revision: 253546
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 3.9-3mdv2008.1
+ Revision: 127992
- kill re-definition of %%buildroot on Pixel's request


* Sun May 14 2006 Olivier Blin <blino@mandriva.com> 3.9-3mdk
- lowercase package name
- mkrel please
- MIT License
- remove world-writable directories and files
- install in gamesdatadir

* Wed Apr 19 2006 Nicolas Chipaux <chipaux@mandriva.com> 3.9-2mdk
- no mkrel please

* Wed Apr 12 2006 Nicolas Chipaux <chipaux@mandriva.com> 3.9-1mdk
- first for mandriva

