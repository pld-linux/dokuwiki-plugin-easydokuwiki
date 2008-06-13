%define		plugin		easydokuwiki
Summary:	DokuWiki Include Plugin
Summary(pl.UTF-8):	Wtyczka Include (dołączania) dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://resources.neolao.com/download/xul/easydokuwiki/easydokuwiki.zip
# Source0-md5:	7a50747fcf617e6d027bfb6f9c5f76e5
URL:		http://resources.neolao.com/xul/easydokuwiki
Requires:	dokuwiki >= 20061008
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Easy Dokuwiki is a Firefox extension that allows navigate, and manage a site in
Dokuwiki.

This is the extension for Dokuwiki for that plugin.

%description -l fr.UTF-8
Easy Dokuwiki est une extension Firefox qui permet de parcourir et de gérer un
site sous Dokuwiki.

C'est la prorogation pour DokuWiki pour ce plugin.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/action.php
