# Increase log verbosity
log_level = "DEBUG"

# Setup data dir
data_dir = "/tmp/server2"

datacenter = "bv1"
log_file = "/home/automation/homecore/deployment/nomad/logs/server.log"

server {
  enabled          = true
  bootstrap_expect = 2

  # This is the IP address of the first server provisioned
  server_join {
    retry_join = [
      "127.0.0.1:4648",
      "192.168.88.16:4648",
      "192.168.88.62:4648",
      "192.168.88.66:4648",
    ]
  }
}

