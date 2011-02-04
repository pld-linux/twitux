Summary:	Twitux - a GTK+ Twitter client
Summary(pl.UTF-8):	Twitux - oparty na GTK+ klient Twittera
Name:		twitux
Version:	0.69
Release:	2
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/twitux/%{name}-%{version}.tar.bz2
# Source0-md5:	e51162151cc59623d95a0cfe3624d254
URL:		http://live.gnome.org/DanielMorales/Twitux
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	enchant-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	iso-codes >= 0.35
BuildRequires:	libcanberra-gtk-devel >= 0.4
BuildRequires:	libnotify-devel
BuildRequires:	libsexy-devel
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.16
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twitux is a GTK+ Twitter client.

%description -l pl.UTF-8
Twitux jest opartym na GTK+ klientem Twittera.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
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
