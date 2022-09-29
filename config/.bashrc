# ssh-agent configuration
if [ -z "$(pgrep ssh-agent)" ]; then
	    rm -rf /tmp/ssh-*
	        eval $(ssh-agent -s) > /dev/null
	else
		    export SSH_AGENT_PID=$(pgrep ssh-agent)
		        export SSH_AUTH_SOCK=$(find /tmp/ssh-* -name agent.*)
fi

ssh-add ~/.ssh/id_rsa
ssh-add ~/.ssh/autotest.pem
ssh-add ~/.ssh/sadogit

copySSHKeys() { cat ~/.ssh/sadogit.pub | ssh $1 "mkdir -p ~/.ssh/; cat >> ~/.ssh/authorized_keys;"; }
copyK8Sconfig() { [[ -z "$2" ]] && echo "$0 <IP> <name>" && return; ssh $1 sudo cat /root/.kube/config > ~/.kube/config_$2 && ln -sf ~/.kube/config_$2 ~/.kube/config; }

