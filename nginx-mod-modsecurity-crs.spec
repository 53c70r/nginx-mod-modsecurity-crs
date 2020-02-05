%global debug_package %{nil}

Name:           nginx-mod-modsecurity-crs
Epoch:          1
Version:        3.2.0
Release:        1%{?dist}
Summary:        OWASP-CRS for Nginx
License:        ASL 2.0
URL:            https://owasp.org/www-project-modsecurity-core-rule-set/
Group:          System Environment/Daemons
Source0:        https://github.com/SpiderLabs/owasp-modsecurity-crs/archive/v%{version}.tar.gz
Source1:        load_file.conf
Source2:        modsecurity.conf

Requires:       nginx

%description
The OWASP ModSecurity Core Rule Set (CRS) is a set of generic attack detection rules for use with ModSecurity or compatible web application firewalls. The CRS aims to protect web applications from a wide range of attacks, including the OWASP Top Ten, with a minimum of false alerts.

%prep
%setup -c -q

%build

%install
%{__install} -d %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/owasp-modsecurity-crs/rules/
%{__install} -p -D -m 644 ./owasp-modsecurity-crs-%{version}/rules/* %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/owasp-modsecurity-crs/rules/
%{__install} -p -D -m 644 ./owasp-modsecurity-crs-%{version}/crs-setup.conf.example %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/owasp-modsecurity-crs/crs-setup.conf
%{__install} -p -D -m 644 ./owasp-modsecurity-crs-%{version}/LICENSE %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/owasp-modsecurity-crs/LICENSE
%{__install} -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/nginx/modsecurity.d/owasp-modsecurity-crs/load_file.conf
%{__install} -p -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/nginx/conf.d/modsecurity.conf

%files
%defattr (-,root,root)
%{_sysconfdir}/nginx/modsecurity.d
%{_sysconfdir}/nginx/conf.d/modsecurity.conf

