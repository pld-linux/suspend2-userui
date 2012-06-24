
%bcond_with	static		# don't use shared libraries
%bcond_without	usplash		# build usplash UI
%bcond_without	fbsplash	# don't build fbsplash UI

Summary:	Suspend2 User UI
Summary(de.UTF-8):	Suspend2 Benutzer Interface
Summary(pl.UTF-8):	Interfejs użytkownika dla Suspend2
Name:		suspend2-userui
Version:	0.7.2
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://www.suspend2.net/downloads/all/%{name}-%{version}.tar.gz
# Source0-md5:	7403ebf48a598ba13d5155b2660a06df
Patch0:		%{name}-Makefile.patch
URL:		http://www.suspend2.net/
BuildRequires:	autoconf
BuildRequires:	automake
%if %{with fbsplash}
BuildRequires:	freetype-devel
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel >= 1.2.12
BuildRequires:	zlib-devel
%if %{with static}
BuildRequires:	freetype-static
BuildRequires:	glibc-static
BuildRequires:	lcms-static
BuildRequires:	libjpeg-static
BuildRequires:	libmng-static
BuildRequires:	libpng-static >= 1.2.12
BuildRequires:	zlib-static
%endif
%endif
%if %{with usplash}
BuildRequires:	usplash-devel >= 0.5.2
%endif
Requires:	hibernate >= 1.93
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Suspend2-userui allows you to use a user interface while hibernating
your laptop. There is a text-ui and a graphical fbsplash-ui/usplash-ui
available.

%description -l de.UTF-8
Suspend2-userui erlaubt es dir ein Benutzer Interface zu nutzen wenn
du deinen Laptop einfrierst. Ein Tekst-UI und graphische UIs
(fbsplash/usplash) stehen zur Verfügung.

%description -l pl.UTF-8
Suspend2-userui pozwala na używanie interfejsu użytkownika w procesie
hibernacji laptopa. Dostępny jest tryb tekstowy oraz graficzny
(fbsplash/usplash).

%package fbsplash
Summary:	Suspend2 User UI for fbsplash
Summary(de.UTF-8):	Suspend2 Benutzer Interface für fbsplash
Summary(pl.UTF-8):	Interfejs użytkownika dla Suspend2 używającego fbsplash
Group:		Applications/System

%description fbsplash
This package provides the fbsplash UI.

%description fbsplash -l de.UTF-8
Dieses Paket enthält das fbsplash UI.

%description fbsplash -l pl.UTF-8
Ta paczka zawiera UI dla fbsplasha.

%package usplash
Summary:	Suspend2 User UI for usplash
Summary(de.UTF-8):	Suspend2 Benutzer Interface für usplash
Summary(pl.UTF-8):	Interfejs użytkownika dla Suspend2 używającego usplash
Group:		Applications/System

%description usplash
This package provides the usplash UI.

%description usplash -l de.UTF-8
Dieses Paket enthält das usplash UI.

%description usplash -l pl.UTF-8
Ta paczka zawiera UI dla usplasha.

%prep
%setup -q
%patch0 -p1

%build
%{__make} clean
%{__make} tuxoniceui_text \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	%{?with_static:LDFLAGS="-static"}

%ifarch !ppc
%if %{with fbsplash}
%{__make} -C fbsplash
	CC="%{__cc}"
	CFLAGS="%{rpmcflags}"
	%{?with_static:LDFLAGS="-static"}

%{__make} tuxoniceui_fbsplash \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	%{?with_static:LDFLAGS="-static"}
%endif

%if %{with usplash}
%{__make} -C usplash
	CC="%{__cc}"
	CFLAGS="%{rpmcflags}"
	%{?with_static:LDFLAGS="-static"}

%{__make} tuxoniceui_usplash \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	%{?with_static:LDFLAGS="-static"}
%endif
%endif # arch

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install tuxoniceui_text $RPM_BUILD_ROOT%{_sbindir}
%ifarhc !ppc
%if %{with fbsplash}
install tuxoniceui_fbsplash $RPM_BUILD_ROOT%{_sbindir}
%endif
%if %{with usplash}
install tuxoniceui_usplash $RPM_BUILD_ROOT%{_sbindir}
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README USERUI_API KERNEL_API
%attr(755,root,root) %{_sbindir}/tuxoniceui_text

%ifarch !ppc
%if %{with fbsplash}
%files fbsplash
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tuxoniceui_fbsplash
%endif

%if %{with usplash}
%files usplash
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tuxoniceui_usplash
%endif
%endif
