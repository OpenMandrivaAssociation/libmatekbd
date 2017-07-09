%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major	4
%define libname	%mklibname matekbd  %{major}
%define libui	%mklibname matekbdui  %{major}
%define devname %mklibname -d matekbd
%define _disable_rebuild_configure 1

Summary:	MATE keyboard libraries
Name:		libmatekbd
Version:	1.18.2
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libxklavier)

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides files used by MATE keyboard library.

#---------------------------------------------------------------------------

%package data
Summary:	Data files and translations for %{name}
Group:		%{group}
BuildArch:	noarch
%rename	%{name}

%description data
This package contains the data files and translation for %{name}.

%files data -f %{name}.lang
%doc NEWS ChangeLog
%{_datadir}/glib-2.0/schemas/org.mate.peripherals-keyboard-xkb.gschema.xml
%dir %{_datadir}/libmatekbd/
%{_datadir}/libmatekbd/*
%{_datadir}/gir-1.0/Matekbd-1.0.gir
%{_libdir}/girepository-1.0/Matekbd-1.0.typelib

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Dynamic libraries for MATE applications
Group:		%{group}
Requires:	%{name}-data >= %{version}-%{release}

%description -n %{libname}
This package contains is part of MATE keyboard library.

%files -n %{libname}
%{_libdir}/libmatekbd.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{libui}
Summary:	Dynamic libraries for MATE applications
Group:		%{group}
Requires:	%{name}-data >= %{version}-%{release}
Conflicts:	%{_lib}matekbd4 < 1.8.0-1

%description -n %{libui}
This package contains is part of MATE keyboard library

%files -n %{libui}
%{_libdir}/libmatekbdui.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development libraries, include files for MATE
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libui} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains libraries and includes files for developing programs
based on the MATE keyboard library.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-introspection=yes \
	--disable-schemas-compile \
	%{nil}
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

