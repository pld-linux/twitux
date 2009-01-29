Summary:	Twitux - a GTK+ Twitter client
Name:		twitux
Version:	0.69
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/twitux/%{name}-%{version}.tar.bz2
# Source0-md5:	e51162151cc59623d95a0cfe3624d254
URL:		http://live.gnome.org/DanielMorales/Twitux
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	enchant-devel >= 1.2.0
BuildRequires:	glib2-devel >= 1:2.15.5
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	iso-codes >= 0.35
BuildRequires:	libcanberra-gtk-devel >= 0.4
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.16
BuildRequires:	pkgconfig
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twitux is a GTK+ Twitter client.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install twitux.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall twitux.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/twitux
%{_sysconfdir}/gconf/schemas/twitux.schemas
%{_desktopdir}/twitux.desktop
%{_iconsdir}/hicolor/*/apps/twitux.png
%{_iconsdir}/hicolor/scalable/apps/twitux.svg
%{_datadir}/twitux
