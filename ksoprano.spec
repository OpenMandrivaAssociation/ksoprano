Summary:	GUI for querying and manipulating RDF data
Name:		ksoprano
Version:	0.2
Release:	4
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://kde-apps.org/content/show.php?content=116756
Source0:	116756-%{name}.tgz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(soprano)

%description
KSoprano is a GUI for querying and manipulating RDF data.

%files
%{_kde_bindir}/ksoprano
%{_kde_appsdir}/ksoprano/ksopranoui.rc

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

