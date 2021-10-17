%global debug_package %{nil}

Name:           nginx-mod-modsecurity-crs
Version:        3.3.2
Release:        4%{?dist}
Summary:        OWASP-CRS for Nginx
License:        ASL 2.0
BuildArch:      noarch
URL:            https://owasp.org/www-project-modsecurity-core-rule-set/
Group:          System Environment/Daemons
Source0:        https://github.com/coreruleset/coreruleset/archive/v%{version}.tar.gz
Source1:        load_file.conf
Source2:        modsecurity.conf

Obsoletes:      mod_security_crs
Requires:       nginx-mod-modsecurity

%description
The OWASP ModSecurity Core Rule Set (CRS) is a set of generic attack detection rules for
use with ModSecurity or compatible web application firewalls. The CRS aims to protect web
applications from a wide range of attacks, including the OWASP Top Ten, with a minimum of false alerts.

%prep
%autosetup -n coreruleset-%{version} -S git

%install
%{__install} -d %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/coreruleset/rules/
%{__install} -p -D -m 0644 ./coreruleset-%{version}/rules/* %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/coreruleset/rules/
%{__install} -p -D -m 0644 ./coreruleset-%{version}/crs-setup.conf.example %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/coreruleset/crs-setup.conf
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/coreruleset/load_file.conf
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/nginx/conf.d/modsecurity.conf

%files
%config(noreplace) %{_sysconfdir}/nginx/modsecurity.d/coreruleset/crs-setup.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/modsecurity.conf
%{_sysconfdir}/nginx/modsecurity.d/coreruleset
%{_sysconfdir}/nginx/conf.d/modsecurity.conf
%license LICENSE
