Name:		texlive-changes
Version:	59950
Release:	2
Summary:	Manual change markup
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/changes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to manually markup changes of text,
such as additions, deletions, or replacements. Changed text is
shown in a different colour; deleted text is crossed out. The
package allows definition of additional authors and their
associated colour. It also allows you to define a markup for
authors or annotations. A bash script is provided for removing
the changes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/changes
%doc %{_texmfdistdir}/doc/latex/changes
#- source
%doc %{_texmfdistdir}/source/latex/changes

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
