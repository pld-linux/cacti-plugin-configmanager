%define		namesrc	configmanager	
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - for download/upload routers switches configuration
Summary(pl.UTF-8):	Wtyczka do Cacti - 
Name:		cacti-plugin-configmanager
Version:	0.75
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	%{namesrc}%{version}.zip
# Source0-md5:	b84133d0eb4b77cfa5159c414ea1f344
Source1:	sharednetworkclass0.36.zip
# Source1-md5:	bd899585510bff2aefbd892b00253a91
URL:		http://forums.cacti.net/about12406.html
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - configmanager
With this plugin you can easily schedule the download/upload of the
configuration of your routers, switches and any devices (or change in
one click some parameters of hundert of switches ... dangerous but
possible now). It should function for all type of router or switches. 

%description -l pl.UTF-8
Wtyczka do Cacti - 

%prep
%setup -q -c -a1

# undos the source
find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}

cd %{namesrc}%{version} 
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{namesrc}%{version}/{Manual.txt,template.txt,configmanager_trap_list.txt} 
%{webcactipluginroot}
