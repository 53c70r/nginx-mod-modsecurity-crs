%global debug_package %{nil}

Name:           nginx-mod-modsecurity-crs
Version:        3.3.0
Release:        3%{?dist}
Summary:        OWASP-CRS for Nginx
License:        ASL 2.0
BuildArch:      noarch
URL:            https://owasp.org/www-project-modsecurity-core-rule-set/
Group:          System Environment/Daemons
Source0:        https://github.com/coreruleset/coreruleset/archive/v%{version}.tar.gz
Source1:        load_file.conf
Source2:        modsecurity.conf
Source3:        LICENSE

Requires:       nginx-mod-modsecurity

%description
The OWASP ModSecurity Core Rule Set (CRS) is a set of generic attack detection rules for use with ModSecurity or compatible web application firewalls. The CRS aims to protect web applications from a wide range of attacks, including the OWASP Top Ten, with a minimum of false alerts.

%prep
%setup -c -q

%build

%install
%{__install} -d %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/coreruleset/rules/
%{__install} -p -D -m 644 %{SOURCE3} %{buildroot}%{_datarootdir}/licenses/%{NAME}/LICENSE
%{__install} -p -D -m 644 ./coreruleset-%{version}/rules/* %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/coreruleset/rules/
%{__install} -p -D -m 644 ./coreruleset-%{version}/crs-setup.conf.example %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/coreruleset/crs-setup.conf
%{__install} -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/coreruleset/load_file.conf
%{__install} -p -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/nginx/conf.d/modsecurity.conf

%files
%defattr (-,root,root)
%{_datarootdir}/licenses/%{NAME}/LICENSE
%{_sysconfdir}/nginx/modsecurity.d
%{_sysconfdir}/nginx/conf.d/modsecurity.conf
%config(noreplace) %{_sysconfdir}/nginx/modsecurity.d/coreruleset/crs-setup.conf
