Summary:	A utility which aims to decrease X session startup time
Summary(de):	Startet ein X-Programm und wartet auf dessen Fenster
Summary(es):	Dispara un programa X y espera por su ventana
Summary(fr):	Lance un programme X et attend sa fen�tre
Summary(tr):	X program� a�ar ve penceresini bekler
Summary(pl):	Narz�dzie maj�ce na celu zmniejszenie czasu startu sesji X
Summary(pt_BR):	Dispara um programa X e espera pela sua janela
Summary(ru):	�������, ���������� ��������� ����� ������� ������ X Window
Summary(uk):	���̦��, �� ��������� �������� ��� ������� ������ X Window
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
Fensters. Kein Endbenutzer-Programm, jedoch n�tzlich zum Schreiben von
Skripts, die X-Windows-Programme ausf�hren.

%description -l es
Utilitario para iniciar un programa y esperar por �l, para hacer el
mapa de una ventana. ENOes un programa "end-user", pero es �til para
escribir scripts que ejecuten programas X Window.

%description -l fr
Utilitaire pour lancer un programme et attendre qu'il corresponde �
une fen�tre. Utile pour �crire des scripts qui lancent des programmes
X Window

%description -l tr
Bir program� �al��t�r�r ve penceresinin yarat�lmas�n� bekler. Son
kullan�c�ya y�nelik bir uygulama de�ildir.

%description -l pl
Xtoolwait jest narz�dziem, kt�re uruchamia X klienta w tle, czeka na
okienko, kt�re ma by� podmapowane w g��wnym oknie, po czym ko�czy
dzia�anie. Xtoolwait mo�e zwi�kszy� wydajno�� dla u�ytkownik�w, kt�rzy
uruchamiaj� du�o klient�w X automatycznie (np. xterm, xlock, xconsole,
cokolwiek) przy starcie sesji X.

%description -l uk
Xtoolwait - �� ���̦��, ��� �������� X �̦���� � �������� ����ͦ,
����� ���� צ� צ���ɤ ��Ϥ צ��� � ������դ����. Xtoolwait ����
��������� ��� ������� ��� ���������ަ�, ���Ҧ ���������� ����� X
�̦��Ԧ� ����������� (���������, xterm, xlock, xconsole � �.�.) ���
������� ������ X Window.

%description -l pt_BR
Utilit�rio para iniciar um programa e esperar por ele para mapear uma
janela. N�o � um programa "end-user", mas � �til para escrever scripts
que rodem programas X Window.

%description -l ru
Xtoolwait - ��� �������, ������� ��������� X ������� � ������� ������,
���� ���� �� ������� ���� ���� � ����� �����������. Xtoolwait �����
�������� ����� ������� ��� �������������, ������� ��������� ����� X
�������� ������������� (��������, xterm, xlock, xconsole, � �.�.) ���
������� ������ X Window.

%description -l uk
Xtoolwait - �� ���̦��, ��� �������� X �̦���� � �������� ����ͦ,
����� ���� צ� צ���ɤ ��Ϥ צ��� � ������դ����. Xtoolwait ����
��������� ��� ������� ��� ���������ަ�, ���Ҧ ���������� ����� X
�̦��Ԧ� ����������� (���������, xterm, xlock, xconsole � �.�.) ���
������� ������ X Window.

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
