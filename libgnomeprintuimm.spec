Summary:	C++ wrappers for libgnomeprintui
Summary(pl):	Interfejsy C++ dla libgnomeprintui
Name:		libgnomeprintuimm
Version:	2.5.0
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	3f25ededb740a3382062105fb7cd3945
URL:		http://www.gnome.org/
BuildRequires:	gtkmm-pango-devel >= 2.3.3
BuildRequires:	libgnomeprintui-devel >= 2.5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgnomeprintui.

%description -l pl
Interfejsy C++ dla libgnomeprintui.

%package devel
Summary:	Devel files for libgnomeprintuimm
Summary(pl):	Pliki nagłówkowe dla libgnomeprintuimm
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtkmm-pango-devel >= 2.3.3

%description devel
Devel files for libgnomeprintuimm.

%description devel -l pl
Pliki nagłówkowe dla libgnomeprintuimm.

%package static
Summary:	libgnomeprintuimm static library
Summary(pl):	Biblioteka statyczna libgnomeprintuimm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libgnomeprintuimm static library.

%description static -l pl
Biblioteka statyczna libgnomeprintuimm.

%prep
%setup -q

%build
%configure \
	--enable-static=yes

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
%attr(755,root,root) %{_libdir}/libgnomeprintuimm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomeprintuimm*.so
%{_libdir}/libgnomeprintuimm*.la
%{_includedir}/%{name}-2.6
%{_libdir}/%{name}-2.6
%{_libdir}/%{name}-2.0
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomeprintuimm*.a
