FROM centos:7
EXPOSE 443
RUN yum install -y nmap-ncat
ENTRYPOINT /bin/sh -c "ncat -l 443 -k -c 'xargs -n1 echo reply\#'"
