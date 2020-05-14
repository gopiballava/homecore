# Ongoing notes for setting up new Raspberry Pi

## Basic bootstrapping

- Use the fancy GUI tool to write a new flash image
- Boot a Pi with a keyboard and monitor (No, it is not as easy as you'd expect to set it up remotely with wireless...)
- `sudo raspi-config` and add your WiFi credentials, change keyboard layout from UK to US
- Turn on remote SSH access
- Set up a real password for the `pi` user
- Create whatever user account you're going to use
- `apt-get update; apt-get upgrade`
- `apt-get install git`
- `ssh-keygen`
- Add your keys to `.ssh/authorized_keys`

## github
- Add your public key to your ssh account

## Nomad
- https://nomadproject.io/downloads/ https://releases.hashicorp.com/nomad/0.11.0/nomad_0.11.0_linux_arm.zip
- `unzip nomad<TAB>`
- FAIL - doesn't work on older Pi....
- https://github.com/bltavares/nomad/releases
- Trying with nomad-0.9
- `~/nomad agent -config server.hcl`
- `nomad agent -config client1.hcl`

in rc.local:

cd /home/automation/homecore/deployment/nomad/
./pi_boot.sh &

## Hostnames
- landing-front-door-camera-pi 192.168.88.66 armv7l nomad 0.11
- freezer-pi 192.168.88.62 armv7l nomad 0.11
-

