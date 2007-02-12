
%define         _name sparkling

Summary:	KDE icons - %{_name}
Summary(pl.UTF-8):   Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	0.5
Release:	1
License:	Artistic 2.0
Group:		Themes
Source0:	http://da-flow.schaekel.org/da-flow/daten/%{_name}_%{version}.tar.gz
# Source0-md5:	3810c8da770787520b7b948447e132cc
URL:		http://kde-look.org/content/show.php?content=9245
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE icons - %{name}.

%description -l pl.UTF-8
Motyw ikon do KDE - %{name}.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
