%define _requires_exceptions perl(GBF::Make)

%define name	gnome-build
%define version 2.24.1

%define api_version 1
%define lib_major 2
%define libname_basic gbf
%define libname %mklibname %{libname_basic} %{api_version} %{lib_major}
%define develname %mklibname -d %{libname_basic}

Summary:	Automake/conf-based project managing framework for GNOME
Name:		%{name}
Version:	%{version}
Release:	%mkrel 4
License:	GPLv2+
Group:		Development/GNOME and GTK+
URL:		http://www.gnome.org/projects/devtools/gnomebuild.shtml
Source01:	ftp://ftp.gnome.org/pub/gnome/sources/%{name}/2.24/%{name}-%{version}.tar.bz2
BuildRequires:  intltool libgdl-devel pkgconfig(libgnomeui-2.0)
BuildRequires:  pkgconfig(libglade-2.0) >= 2.0.1

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


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.24.1-4mdv2011.0
+ Revision: 610917
- rebuild

* Sun Jan 31 2010 Funda Wang <fwang@mandriva.org> 2.24.1-3mdv2010.1
+ Revision: 498671
- Br glade

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 2.24.1-2mdv2009.1
+ Revision: 301579
- rebuilt against new libxcb

* Wed Oct 22 2008 Funda Wang <fwang@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 296511
- New version 2.24.1

* Tue Sep 23 2008 Funda Wang <fwang@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287177
- BR gnomeui
- python-gdl is not needed
- New version 2.24.0

* Mon Aug 25 2008 Funda Wang <fwang@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 275592
- New version 2.23.90

* Wed Jul 09 2008 Funda Wang <fwang@mandriva.org> 0.3.0-1mdv2009.0
+ Revision: 233089
- New version 0.3.0

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Apr 15 2008 Funda Wang <fwang@mandriva.org> 0.2.4-1mdv2009.0
+ Revision: 193633
- New version 0.2.4

* Sat Feb 02 2008 Funda Wang <fwang@mandriva.org> 0.2.1-1mdv2008.1
+ Revision: 161354
- correct libname
- New version 0.2.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 08 2007 Funda Wang <fwang@mandriva.org> 0.2.0-1mdv2008.0
+ Revision: 82437
- fix building
- new major of library
- New versino 0.2.0

* Wed Jun 27 2007 Funda Wang <fwang@mandriva.org> 0.1.7-1mdv2008.0
+ Revision: 45053
- More simplified develpackage name
- fix file list
- New version

* Sun May 13 2007 Funda Wang <fwang@mandriva.org> 0.1.6-1mdv2008.0
+ Revision: 26527
- New upstream version

* Mon Apr 30 2007 Lenny Cartier <lenny@mandriva.org> 0.1.4-5mdv2008.0
+ Revision: 19702
- requires exception on perl module


* Thu Mar 01 2007 Jérôme Soyer <saispo@mandriva.org> 0.1.4-4mdv2007.0
+ Revision: 130501
- Bump Release
- Fix BR
- Fix BR
- Import gnome-build

