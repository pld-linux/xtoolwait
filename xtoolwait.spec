Summary:	A utility which aims to decrease X session startup time
Summary(de):	Startet ein X-Programm und wartet auf dessen Fenster
Summary(es):	Dispara un programa X y espera por su ventana
Summary(fr):	Lance un programme X et attend sa fenЙtre
Summary(tr):	X programЩ aГar ve penceresini bekler
Summary(pl):	NarzЙdzie maj╠ce na celu zmniejszenie czasu startu sesji X
Summary(pt_BR):	Dispara um programa X e espera pela sua janela
Summary(ru):	Утилита, помогающая уменьшить время запуска сеанса X Window
Summary(uk):	Утил╕та, що допомага╓ зменшити час запуску сеансу X Window
Name:		xtoolwait
Version:	1.3
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.x.org/contrib/utilities/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Xtoolwait is a utility which starts an X client in the background,
waits for a window to be mapped on the root window, and then exits.
Xtoolwait can improve performance for users who start a bunch of X
clients automatically (for example, xterm, xlock, xconsole, whatever)
when the X session starts.

Install xtoolwait if you'd like to try to speed up the startup time
for X sessions.

%description -l de
Utility zum Starten eines Programms und Abwarten des Aufbaus eines
Fensters. Kein Endbenutzer-Programm, jedoch nЭtzlich zum Schreiben von
Skripts, die X-Windows-Programme ausfЭhren.

%description -l es
Utilitario para iniciar un programa y esperar por Иl, para hacer el
mapa de una ventana. ENOes un programa "end-user", pero es Зtil para
escribir scripts que ejecuten programas X Window.

%description -l fr
Utilitaire pour lancer un programme et attendre qu'il corresponde Ю
une fenЙtre. Utile pour Иcrire des scripts qui lancent des programmes
X Window

%description -l tr
Bir programЩ ГalЩЧtЩrЩr ve penceresinin yaratЩlmasЩnЩ bekler. Son
kullanЩcЩya yЖnelik bir uygulama deПildir.

%description -l pl
Xtoolwait jest narzЙdziem, ktСre uruchamia X klienta w tle, czeka na
okienko, ktСre ma byФ podmapowane w gЁСwnym oknie, po czym koЯczy
dziaЁanie. Xtoolwait mo©e zwiЙkszyФ wydajno╤Ф dla u©ytkownikСw, ktСrzy
uruchamiaj╠ du©o klientСw X automatycznie (np. xterm, xlock, xconsole,
cokolwiek) przy starcie sesji X.

%description -l uk
Xtoolwait - це утил╕та, яка запуска╓ X кл╕╓нта в фоновому режим╕,
чека╓ доки в╕н в╕дкри╓ сво╓ в╕кно ╕ завершу╓ться. Xtoolwait може
покращити час запуску для користувач╕в, котр╕ запускають пакет X
кл╕╓нт╕в автоматично (наприклад, xterm, xlock, xconsole ╕ т.п.) при
запуску сеансу X Window.

%description -l pt_BR
UtilitАrio para iniciar um programa e esperar por ele para mapear uma
janela. NЦo И um programa "end-user", mas И Зtil para escrever scripts
que rodem programas X Window.

%description -l ru
Xtoolwait - это утилита, которая запускает X клиента в фоновом режиме,
ждет пока он откроет свое окно и затем завершается. Xtoolwait может
улучшить время запуска для пользователей, которые запускают пакет X
клиентов автоматически (например, xterm, xlock, xconsole, и т.п.) при
запуске сеанса X Window.

%description -l uk
Xtoolwait - це утил╕та, яка запуска╓ X кл╕╓нта в фоновому режим╕,
чека╓ доки в╕н в╕дкри╓ сво╓ в╕кно ╕ завершу╓ться. Xtoolwait може
покращити час запуску для користувач╕в, котр╕ запускають пакет X
кл╕╓нт╕в автоматично (наприклад, xterm, xlock, xconsole ╕ т.п.) при
запуску сеансу X Window.

%prep
%setup -q

%build
xmkmf
%{__make} \
	CC="%{__cc}" \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/xtoolwait
%{_mandir}/man1/xtoolwait.1x*
