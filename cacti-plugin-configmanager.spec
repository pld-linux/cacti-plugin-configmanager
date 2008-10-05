# TODO
# - source1 not used?!
%define		plugin configmanager
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - download/upload routers and switches configuration
Summary(pl.UTF-8):	Wtyczka do Cacti - ściąganie/wysyłanie konfiguracji routerów/switchy
Name:		cacti-plugin-%{plugin}
Version:	0.76
Release:	1
License:	GPL v2
Group:		Applications/WWW
# http://forums.cacti.net/download.php?id=6449
Source0:	%{plugin}%{version}.zip
# Source0-md5:	d3cdb035a4d47ff464916774dd953457
# http://forums.cacti.net/download.php?id=10980
Source1:	sharednetworkclass0.40.zip
# Source1-md5:	b438751d7b696a10a8958ea6e0f407f3
URL:		http://forums.cacti.net/about12406.html
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
With Cacti configmanager plugin you can easily schedule the
download/upload of the configuration of your routers, switches and any
devices (or change in one click some parameters of a hundred of
switches... dangerous but possible now). It should function for all
type of router or switches.

There are two methods:
- "TFTP" (based of "pancho" <http://www.pancho.org/>); with "pure PHP"
  option there is no need of pancho installation
- "multi" can use any scripts or SCP, FTP, SFTP or what you want.

%description -l pl.UTF-8
Przy użyciu wtyczki Cacti configmanager można łatwo zaszeregować
ściąganie lub wysyłanie konfiguracji routerów, switchy i innych
urządzeń (lub zmieniać jednym kliknięciem pewne parametry w setce
switchy... co jest niebezpieczne, ale teraz wykonalne). Wtyczka
powinna działać z dowolnymi routerami i switchami.

Istnieją dwie metody:
- "TFTP" (oparta na "pancho" <http://www.pancho.org/>); z opcją "pure
  PHP" nie ma potrzeby instalacji pancho
- "multi", potrafiąca używać dowolne skrypty lub SCP, FTP, SFTP

%prep
%setup -qc -a1

# undos the source
find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}

cp -a %{plugin}%{version}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{plugin}%{version}/{Manual.txt,template.txt,configmanager_trap_list.txt}
%{plugindir}
