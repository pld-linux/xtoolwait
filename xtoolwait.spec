Summary: A utility which aims to decrease X session startup time.
Name: xtoolwait
Version: 1.2
Release: 2
Copyright: GPL
Group: Applications/System
Source: ftp://ftp.x.org/contrib/utilities/xtoolwait-1.2.tar.gz
Prefix: /usr
BuildRoot: /var/tmp/xtoolwait-root

%description
Xtoolwait is a utility which starts an X client in the background, waits
for a window to be mapped on the root window, and then exits.  Xtoolwait
can improve performance for users who start a bunch of X clients
automatically (for example, xterm, xlock, xconsole, whatever) when the
X session starts.

Install xtoolwait if you'd like to try to speed up the startup time for
X sessions.

%prep
%setup -q

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xtoolwait
/usr/X11R6/man/man1/xtoolwait.1x
