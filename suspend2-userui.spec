Summary:	Suspend2 User UI
Summary(de):	Suspend2 Benutzer Interface
Summary(pl):	Interfejs u¿ytkownika dla Suspend2
Name:		suspend2-userui
Version:	0.6.4
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://www.suspend2.net/downloads/all/%{name}-%{version}.tar.gz
# Source0-md5:	737427dd2eb076907674a4334735c2ef
Patch0:		%{name}-Makefile.patch
URL:		http://www.suspend2.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
Requires:	hibernate >= 1.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Suspend2-userui allows you use a user interface while hibernating your
laptop. There is a text-ui and a graphical fbsplash-ui available.

%description -l de
Suspend2-userui erlaubt es dir ein Benutzer Interface zu nutzen wenn
du deinen Laptop einfrierst. Ein Tekst-UI und ein graphisches UI
stehen zur Verfügung.

%description -l pl
Suspend2-userui pozwala na u¿ywanie interfejsu u¿ytkownika w procesie
hibernacji laptopa. Dostêpny jest tryb tekstowy oraz graficzny
(fbsplash).

%prep
%setup -q
%patch0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

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
