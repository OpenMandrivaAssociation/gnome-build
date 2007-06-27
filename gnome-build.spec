%define _requires_exceptions perl(GBF::Make)

%define name	gnome-build
%define version 0.1.7

%define api_version 1
%define lib_major 0
%define libname_basic gbf
%define libname %mklibname %{libname_basic}- %{api_version} %{lib_major}
%define develname %mklibname -d %{libname_basic}- %{api_version}

Summary:	Automake/conf-based project managing framework for GNOME
Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
License:	GPL
Group:		Development/GNOME and GTK+
URL:		http://www.gnome.org/projects/devtools/gnomebuild.shtml
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		ftp://ftp.gnome.org/pub/gnome/sources/%{name}/0.1/%{name}-%{version}.tar.bz2
BuildRequires:	gtk2-devel
BuildRequires:	libgdl-devel
BuildRequires:	libxml2-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libgnome2-devel
BuildRequires:	libbonoboui2-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:	gnome-common
BuildRequires:  intltool, libtool, gettext, libgdl-devel, gdl, gnome-python-gdl

%description
Gnome-build is a GObject-based framework for managing projects and
specifically automake/conf-based projects.  It can parse the
configure.in and Makefile.am files to build an internal XML
representation of the project.

%package	-n %{libname}
Summary:	Automake/conf-based project managing framework for GNOME
Group:		System/Libraries

%description	-n %{libname}
Gnome-build is a GObject-based framework for managing projects and
specifically automake/conf-based projects.  It can parse the
configure.in and Makefile.am files to build an internal XML
representation of the project.

This package contains main libraries for Gnome-build Framework.

%package	-n %{develname}
Summary:	Header and development for Gnome Build Framework
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{libname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel < 0.1.7 

%description	-n %{develname}
Gnome-build is a GObject-based framework for managing projects and
specifically automake/conf-based projects.  It can parse the
configure.in and Makefile.am files to build an internal XML
representation of the project.

This package contains header files and various development files for
compiling or developing applications that need Gnome-build Framework.

%prep
%setup -q

%build
%configure --disable-static
make LIBTOOL=%{_prefix}/bin/libtool

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
make DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
find %{buildroot} -type f -name "*.a" -exec rm -f {} ';'

%define gettext_package gbf-1
%{find_lang} %{gettext_package}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -f %{gettext_package}.lang
%defattr(-, root, root)
%doc AUTHORS MAINTAINERS
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}
%{_libdir}/%{name}-1.0

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(-, root, root)
%doc ChangeLog
%{_includedir}/*
%dir %{_includedir}/gnome-build-1.0
%{_includedir}/gnome-build-1.0
%{_libdir}/lib*.so
#%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*
