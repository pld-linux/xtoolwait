Summary:	A utility which aims to decrease X session startup time
Summary(pl):	Narzêdzie które ma na celu zmniejszenie czasu startu sesji X
Name:		xtoolwait
Version:	1.2
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.x.org/contrib/utilities/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Xtoolwait is a utility which starts an X client in the background,
waits for a window to be mapped on the root window, and then exits.
Xtoolwait can improve performance for users who start a bunch of X
clients automatically (for example, xterm, xlock, xconsole, whatever)
when the X session starts.

Install xtoolwait if you'd like to try to speed up the startup time
for X sessions.

%prep
%setup -q

%build
xmkmf
%{__make} CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xtoolwait
%{_mandir}/man1/xtoolwait.1x*
