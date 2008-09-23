%define _requires_exceptions perl(GBF::Make)

%define name	gnome-build
%define version 2.24.0

%define api_version 1
%define lib_major 2
%define libname_basic gbf
%define libname %mklibname %{libname_basic} %{api_version} %{lib_major}
%define develname %mklibname -d %{libname_basic}

Summary:	Automake/conf-based project managing framework for GNOME
Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
License:	GPLv2+
Group:		Development/GNOME and GTK+
URL:		http://www.gnome.org/projects/devtools/gnomebuild.shtml
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
Source:		ftp://ftp.gnome.org/pub/gnome/sources/%{name}/2.24/%{name}-%{version}.tar.bz2
BuildRequires:  intltool libgdl-devel gnome-python-gdl

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
Provides:	lib%{libname_basic}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d gbf- 1 0

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
export CFLAGS="%{optflags} -D_GNU_SOURCE"
export CXXFLAGS="%{optflags} -D_GNU_SOURCE"
%configure2_5x --disable-static
# fwang: parallel build fails in some unknown cases
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang gbf-1

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -f gbf-1.lang
%defattr(-, root, root)
%doc AUTHORS MAINTAINERS
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}
%{_libdir}/%{name}-1.0

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/lib*.so.%{lib_major}*

%files -n %{develname}
%defattr(-, root, root)
%doc ChangeLog
%{_includedir}/gnome-build-1.0
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*
