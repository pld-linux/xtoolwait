Summary:	A utility which aims to decrease X session startup time
Summary(pl):	Narz�dzie maj�ce na celu zmniejszenie czasu startu sesji X
Name:		xtoolwait
Version:	1.2
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
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

%description -l pl
Xtoolwait jest narz�dziem, kt�re uruchamia X klienta w tle, czeka na
okienko, kt�re ma by� podmapowane w g��wnym oknie, po czym ko�czy
dzia�anie. Xtoolwait mo�e zwi�kszy� wydajno�� dla u�ytkownik�w, kt�rzy
uruchamiaj� du�o klint�w X automatycznie (np. xterm, xlock, xconsole,
cokolwiek) przy starcie sesji X.

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
