Name:		texlive-photobook
Version:	68313
Release:	1
Summary:	A document class for typesetting photo books
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/photobook
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/photobook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/photobook.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX document class extends the book class defining a set
of parameters, meta-macros, macros and environments with
reasonable defaults to help typeset, build and print books
mainly based on visual/image content.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/photobook
%doc %{_texmfdistdir}/doc/latex/photobook

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
