%define major	4
%define libname	%mklibname matekbd  %{major}
%define devname %mklibname -d matekbd

Summary:	MATE keyboard libraries
Name:		libmatekbd
Version:	1.4.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(libxklavier)

%description
Files used by MATE keyboard library

%package -n %{libname}
Summary:	Dynamic libraries for MATE applications
Group:		%{group}

%description -n %{libname}
MATE keyboard library

%package -n %{devname}
Summary:	Development libraries, include files for MATE
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development library and headers file needed in order to develop
applications using the MATE keyboard library

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static

%make LIBS='-lm -lgmodule-2.0'

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS ChangeLog
%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_keyboard_xkb.schemas
%{_bindir}/matekbd-indicator-plugins-capplet
%{_datadir}/applications/matekbd-indicator-plugins-capplet.desktop
%{_datadir}/libmatekbd/

%files -n %{libname}
%{_libdir}/libmatekbd*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so



%changelog
* Thu Aug 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.0-1
+ Revision: 811555
- new version 1.4.0

* Thu May 31 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 801661
- imported package libmatekbd

