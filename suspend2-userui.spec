
%bcond_with	static	# don't use shared libraries

Summary:	Suspend2 User UI
Summary(de.UTF-8):	Suspend2 Benutzer Interface
Summary(pl.UTF-8):	Interfejs użytkownika dla Suspend2
Name:		suspend2-userui
Version:	0.7.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.suspend2.net/downloads/all/%{name}-%{version}.tar.gz
# Source0-md5:	7a41e9195597319825ecee0d1f3aa166
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-ppc.patch
URL:		http://www.suspend2.net/
BuildRequires:	autoconf
BuildRequires:	automake
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
Requires:	hibernate >= 1.93
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Suspend2-userui allows you use a user interface while hibernating your
laptop. There is a text-ui and a graphical fbsplash-ui available.

%description -l de.UTF-8
Suspend2-userui erlaubt es dir ein Benutzer Interface zu nutzen wenn
du deinen Laptop einfrierst. Ein Tekst-UI und ein graphisches UI
stehen zur Verfügung.

%description -l pl.UTF-8
Suspend2-userui pozwala na używanie interfejsu użytkownika w procesie
hibernacji laptopa. Dostępny jest tryb tekstowy oraz graficzny
(fbsplash).

%prep
%setup -q
%patch0 -p1

%ifarch ppc
%patch1 -p1
%endif

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	%{?with_static:LDFLAGS="-static"}
	
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README USERUI_API KERNEL_API
%attr(755,root,root) %{_sbindir}/suspend2ui_*
