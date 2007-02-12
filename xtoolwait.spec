Summary:	A utility which aims to decrease X session startup time
Summary(de.UTF-8):   Startet ein X-Programm und wartet auf dessen Fenster
Summary(es.UTF-8):   Dispara un programa X y espera por su ventana
Summary(fr.UTF-8):   Lance un programme X et attend sa fenêtre
Summary(pl.UTF-8):   Narzędzie mające na celu zmniejszenie czasu startu sesji X
Summary(pt_BR.UTF-8):   Dispara um programa X e espera pela sua janela
Summary(ru.UTF-8):   Утилита, помогающая уменьшить время запуска сеанса X Window
Summary(tr.UTF-8):   X programı açar ve penceresini bekler
Summary(uk.UTF-8):   Утиліта, що допомагає зменшити час запуску сеансу X Window
Name:		xtoolwait
Version:	1.3
Release:	5
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.x.org/contrib/utilities/%{name}-%{version}.tar.gz
# Source0-md5:	6db998d882b17b35c9fa858432e345a6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xtoolwait is a utility which starts an X client in the background,
waits for a window to be mapped on the root window, and then exits.
Xtoolwait can improve performance for users who start a bunch of X
clients automatically (for example, xterm, xlock, xconsole, whatever)
when the X session starts.

Install xtoolwait if you'd like to try to speed up the startup time
for X sessions.

%description -l de.UTF-8
Utility zum Starten eines Programms und Abwarten des Aufbaus eines
Fensters. Kein Endbenutzer-Programm, jedoch nützlich zum Schreiben von
Skripts, die X-Window-Programme ausführen.

%description -l es.UTF-8
Utilitario para iniciar un programa y esperar por él, para hacer el
mapa de una ventana. ENOes un programa "end-user", pero es útil para
escribir scripts que ejecuten programas X Window.

%description -l fr.UTF-8
Utilitaire pour lancer un programme et attendre qu'il corresponde à
une fenêtre. Utile pour écrire des scripts qui lancent des programmes
X Window

%description -l tr.UTF-8
Bir programı çalıştırır ve penceresinin yaratılmasını bekler. Son
kullanıcıya yönelik bir uygulama değildir.

%description -l pl.UTF-8
Xtoolwait jest narzędziem, które uruchamia X klienta w tle, czeka na
okienko, które ma być podmapowane w głównym oknie, po czym kończy
działanie. Xtoolwait może zwiększyć wydajność dla użytkowników, którzy
uruchamiają dużo klientów X automatycznie (np. xterm, xlock, xconsole,
cokolwiek) przy starcie sesji X.

%description -l uk.UTF-8
Xtoolwait - це утиліта, яка запускає X клієнта в фоновому режимі,
чекає доки він відкриє своє вікно і завершується. Xtoolwait може
покращити час запуску для користувачів, котрі запускають пакет X
клієнтів автоматично (наприклад, xterm, xlock, xconsole і т.п.) при
запуску сеансу X Window.

%description -l pt_BR.UTF-8
Utilitário para iniciar um programa e esperar por ele para mapear uma
janela. Não é um programa "end-user", mas é útil para escrever scripts
que rodem programas X Window.

%description -l ru.UTF-8
Xtoolwait - это утилита, которая запускает X клиента в фоновом режиме,
ждет пока он откроет свое окно и затем завершается. Xtoolwait может
улучшить время запуска для пользователей, которые запускают пакет X
клиентов автоматически (например, xterm, xlock, xconsole, и т.п.) при
запуске сеанса X Window.

%description -l uk.UTF-8
Xtoolwait - це утиліта, яка запускає X клієнта в фоновому режимі,
чекає доки він відкриє своє вікно і завершується. Xtoolwait може
покращити час запуску для користувачів, котрі запускають пакет X
клієнтів автоматично (наприклад, xterm, xlock, xconsole і т.п.) при
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

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR="%{_bindir}" \
	MANDIR="%{_mandir}/man1"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/xtoolwait
%{_mandir}/man1/xtoolwait.1x*
