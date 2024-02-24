%define mate_ver	%(echo %{version}|cut -d. -f1,2)

%define major	6
%define libname	%mklibname matekbd
%define libui	%mklibname matekbdui
%define devname	%mklibname matekbd -d
%define oldlibname	%mklibname matekbd 3
%define oldlibui	%mklibname matekbdui 4

%define	gimajor	1.0
%define	girname	%mklibname matekbd-gir %{gimajor}

Summary:	MATE keyboard libraries
Name:		libmatekbd
Version:	1.28.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{mate_ver}/%{name}-%{version}.tar.xz

BuildRequires:	autoconf-archive
BuildRequires:	libxml2-utils
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(gio-2.0)
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
%doc NEWS ChangeLog README COPYING
%{_datadir}/glib-2.0/schemas/org.mate.peripherals-keyboard-xkb.gschema.xml

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Dynamic libraries for MATE applications
Group:		%{group}
Requires:	%{name}-data >= %{version}-%{release}
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n %{libname}
This package is part of MATE keyboard library.

%files -n %{libname}
%{_libdir}/libmatekbd.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{libui}
Summary:	Dynamic libraries for MATE applications
Group:		%{group}
Requires:	%{name}-data >= %{version}-%{release}
Conflicts:	%{_lib}matekbd4 < 1.8.0-1
Obsoletes:	%{oldlibui} < %{EVRD}

%description -n %{libui}
This package is part of MATE keyboard library

%files -n %{libui}
%{_libdir}/libmatekbdui.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
This package contains GObject Introspection interface library for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/Matekbd-%{gimajor}.typelib

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
%{_datadir}/gir-1.0/Matekbd-%{gimajor}.gir

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-introspection \
	--disable-schemas-compile \
	%{nil}
%make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome --all-name

