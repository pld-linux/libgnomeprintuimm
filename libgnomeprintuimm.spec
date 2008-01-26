Summary:	C++ wrappers for libgnomeprintui
Summary(pl.UTF-8):	Interfejsy C++ dla libgnomeprintui
Name:		libgnomeprintuimm
Version:	2.5.2
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomeprintuimm/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	e5272e207f40af5116813bb0d92b352d
URL:		http://www.gnome.org/
BuildRequires:	gtkmm-devel >= 2.4.5
BuildRequires:	libgnomeprintmm-devel >= 2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.8.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgnomeprintui.

%description -l pl.UTF-8
Interfejsy C++ dla libgnomeprintui.

%package devel
Summary:	Devel files for libgnomeprintuimm
Summary(pl.UTF-8):	Pliki nagłówkowe dla libgnomeprintuimm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkmm-devel >= 2.4.5
Requires:	libgnomeprintmm-devel >= 2.5.1
Requires:	libgnomeprintui-devel >= 2.8.0

%description devel
Devel files for libgnomeprintuimm.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libgnomeprintuimm.

%package static
Summary:	libgnomeprintuimm static library
Summary(pl.UTF-8):	Biblioteka statyczna libgnomeprintuimm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libgnomeprintuimm static library.

%description static -l pl.UTF-8
Biblioteka statyczna libgnomeprintuimm.

%prep
%setup -q

%build
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgnomeprintuimm-2.5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomeprintuimm-2.5.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomeprintuimm-2.5.so
%{_libdir}/libgnomeprintuimm-2.5.la
%{_includedir}/%{name}-2.6
%{_libdir}/%{name}-2.6
%{_libdir}/%{name}-2.0
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomeprintuimm-2.5.a
