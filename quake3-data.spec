%define	_dataver	1.32b-3
%define _version	%(echo %{_dataver} | tr -d -)

Summary:	Quake3 III Arena additional files
Summary(pl.UTF-8):	Dodatkowe pliki dla Quake III Arena
Name:		quake3-data
Version:	%{_version}
Release:	2
License:	Q3A EULA, PB EULA (non-commercially distributable)
Group:		X11/Applications/Games
Source0:	ftp://ftp.idsoftware.com/idstuff/quake3/linux/linuxq3apoint-%{_dataver}.x86.run
# Source0-md5:	c71fdddccb20e8fc393d846e9c61d685
URL:		http://www.quake3arena.com/
Requires:	quake3-common
Conflicts:	quake3-common < 1.33-0.20051103.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional pak files for Quake III Arena.

%description -l pl.UTF-8
Dodatkowe pliki pak dla Quake III Arena.

%prep
%setup -qcT
sh %{SOURCE0} --tar xf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/quake3/baseq3

install baseq3/pak?.pk3 $RPM_BUILD_ROOT%{_datadir}/games/quake3/baseq3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Q3A_EULA.txt README-linux.txt pb/PB_EULA.txt
%{_datadir}/games/quake3/baseq3/*
