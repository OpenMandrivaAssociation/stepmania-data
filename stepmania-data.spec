%define gamename StepMania
%define distname %{gamename}-data
%define	name	stepmania-data
%define	version	3.9
%define	release	%mkrel 6

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

