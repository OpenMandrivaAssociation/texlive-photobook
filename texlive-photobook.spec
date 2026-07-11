%global tl_name photobook
%global tl_revision 71843

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.31
Release:	%{tl_revision}.1
Summary:	A document class for typesetting photo books
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/photobook
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/photobook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/photobook.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(adjustbox)
Requires:	texlive(atbegshi)
Requires:	texlive(changepage)
Requires:	texlive(colorspace)
Requires:	texlive(environ)
Requires:	texlive(eso-pic)
Requires:	texlive(etoolbox)
Requires:	texlive(fancyhdr)
Requires:	texlive(fancyvrb)
Requires:	texlive(flowfram)
Requires:	texlive(geometry)
Requires:	texlive(graphics)
Requires:	texlive(hyperref)
Requires:	texlive(iftex)
Requires:	texlive(kvoptions)
Requires:	texlive(listofitems)
Requires:	texlive(mdframed)
Requires:	texlive(numprint)
Requires:	texlive(pagecolor)
Requires:	texlive(pdfcomment)
Requires:	texlive(pdfpages)
Requires:	texlive(pgf)
Requires:	texlive(textpos)
Requires:	texlive(xargs)
Requires:	texlive(xcolor)
Requires:	texlive(xint)
Requires:	texlive(xkeyval)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The photobook LaTeX document class extends the book class defining a set
of parameters, meta-macros, macros and environments with reasonable
defaults to help typeset, build and print books mainly based on
visual/image content.

