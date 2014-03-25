%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major	4
%define libname	%mklibname matekbd  %{major}
%define devname %mklibname -d matekbd

Summary:	MATE keyboard libraries
Name:		libmatekbd
Version:	1.8.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
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
NOCONFIGURE=yes ./autogen.sh

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

# remove unneeded converters
rm -fr %{buildroot}%{_datadir}/MateConf

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS ChangeLog
%{_datadir}/glib-2.0/schemas/org.mate.peripherals-keyboard-xkb.gschema.xml
%{_datadir}/libmatekbd/

%files -n %{libname}
%{_libdir}/libmatekbd*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

