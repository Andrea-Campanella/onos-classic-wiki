# Notes on cluster formation for Docker instances

1. Download Atomix docker image:

> $ docker pull atomix/atomix:3.1.5

2. Run three instacnes of Atomix:

> $ docker run -t -d --name atomix-1 atomix/atomix:3.1.5
>
> $ docker run -t -d --name atomix-2 atomix/atomix:3.1.5
>
> $ docker run -t -d --name atomix-3 atomix/atomix:3.1.5

3. Check docker IP of Atomix instances;

> $ docker inspect atomix-1 | grep -i ipaddress
>
> $ docker inspect atomix-2 | grep -i ipaddress
>
> $ docker inspect atomix-3 | grep -i ipaddress

4. Check out ONOS source code:

> $ git clone <https://gerrit.onosproject.org/onos>

5. Set relevant environment variables to docker IP of Atomix instances obtained above:

> $ export OC1=172.17.0.2
>
> $ export OC2=172.17.0.3
>
> $ export OC3=172.17.0.4

6. Generate Atomix configuration files:

> cd /path/to/your/onos/source/root
>
> ./tools/test/bin/atomix-gen-config 172.17.0.2 ~/atomx-1.conf 172.17.0.2 172.17.0.3 172.17.0.4
>
> ./tools/test/bin/atomix-gen-config 172.17.0.3 ~/atomix-2.conf 172.17.0.2 172.17.0.3 172.17.0.4
>
> ./tools/test/bin/atomix-gen-config 172.17.0.4 ~/atomix-3.conf 172.17.0.2 172.17.0.3 172.17.0.4

7. Copy Atomix configuration to docker instances:

> $ docker cp ~/atomix-1.conf atomix-1:/opt/atomix/conf/atomix.conf
>
> $ docker cp ~/atomix-2.conf atomix-2:/opt/atomix/conf/atomix.conf
>
> $ docker cp ~/atomix-3.conf atomix-3:/opt/atomix/conf/atomix.conf

8. Restart Atomix docker instances for configuration to take effect:

> $ docker restart atomix-1
>
> $ docker restart atomix-2
>
> $ docker restart atomix-3

9. Download ONOS docker image:

> $ docker pull onosproject/onos:2.2.2

10. Run three ONOS docker instances:

> $ docker run -t -d --name onos1 onosproject/onos:2.2.2
>
> $ docker run -t -d --name onos2 onosproject/onos:2.2.2
>
> $ docker run -t -d --name onos3 onosproject/onos:2.2.2

11. Check docker IP of ONOS instances;

> $ docker inspect onos1 | grep -i ipaddress
>
> $ docker inspect onos2 | grep -i ipaddress
>
> $ docker inspect onos3 | grep -i ipaddress

12. Generate ONOS cluster configuration files using docker IP obtained above:

> cd /path/to/your/onos/source/root
>
> ./tools/test/bin/onos-gen-config 172.17.0.5 ~/cluster-1.json -n 172.17.0.2 172.17.0.3 172.17.0.4
>
> ./tools/test/bin/onos-gen-config 172.17.0.6 ~/cluster-2.json -n 172.17.0.2 172.17.0.3 172.17.0.4
>
> ./tools/test/bin/onos-gen-config 172.17.0.7 ~/cluster-3.json -n 172.17.0.2 172.17.0.3 172.17.0.4

13. Create config directory for ONOS docker instances:

> $ docker exec onos1 mkdir /root/onos/config
>
> $ docker exec onos2 mkdir /root/onos/config
>
> $ docker exec onos3 mkdir /root/onos/config

14. Copy ONOS cluster configuration to docker instances:

> $ docker cp ~/cluster-1.json onos1:/root/onos/config/cluster.json
>
> $ docker cp ~/cluster-2.json onos2:/root/onos/config/cluster.json
>
> $ docker cp ~/cluster-3.json onos3:/root/onos/config/cluster.json

15. Restart ONOS docker instances for configuration to take effect:

> $ docker restart onos1
>
> $ docker restart onos2
>
> $ docker restart onos3

16. Login ONOS Web UI to check cluster formation.
