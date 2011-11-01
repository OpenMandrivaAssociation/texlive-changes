Name:		texlive-changes
Version:	0.5.4
Release:	1
Summary:	Manual change markup
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/changes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package allows the user to manually markup changes of text,
such as additions, deletions, or replacements. Changed text is
shown in a different colour; deleted text is crossed out. The
package allows definition of additional authors and their
associated colour. It also allows you to define a markup for
authors or annotations. A bash script is provided for removing
the changes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/changes/changes.sty
%doc %{_texmfdistdir}/doc/latex/changes/README
%doc %{_texmfdistdir}/doc/latex/changes/changes.english.full.pdf
%doc %{_texmfdistdir}/doc/latex/changes/changes.english.short.pdf
%doc %{_texmfdistdir}/doc/latex/changes/changes.ngerman.full.pdf
%doc %{_texmfdistdir}/doc/latex/changes/changes.ngerman.short.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.1.de.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.1.de.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.2.de.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.2.de.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.3.de.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.3.de.tex
#- source
%doc %{_texmfdistdir}/source/latex/changes/changes.drv
%doc %{_texmfdistdir}/source/latex/changes/changes.dtx
%doc %{_texmfdistdir}/source/latex/changes/changes.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
