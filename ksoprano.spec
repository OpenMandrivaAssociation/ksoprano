Name:          ksoprano
Version:       0.2
Release:       %mkrel 1
Summary:       GUI for querying and manipulating RDF data
Group:         Graphical desktop/KDE
License:       GPLv2+
Url:           http://kde-apps.org/content/show.php?content=116756
Source:        116756-%name.tgz
BuildRequires: kdelibs4-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root

%description
ksoprano is a GUI for querying and manipulating RDF data.

%files 
%defattr(-,root,root)
%_kde_bindir/ksoprano
%_kde_appsdir/ksoprano/ksopranoui.rc

#--------------------------------------------------------------------

%prep
%setup -q -n %name

%build
%cmake_kde4
%make 

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}