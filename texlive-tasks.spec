Name:		texlive-tasks
Version:	61541
Release:	2
Summary:	Horizontally columned lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tasks
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tasks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tasks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The reason for the creation of the tasks environment was an
unwritten agreement in German maths textbooks (especially
(junior) high school textbooks) to organize exercises in
columns counting horizontally rather than vertically. This is
what the tasks package helps to achieve.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tasks
%doc %{_texmfdistdir}/doc/latex/tasks

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
